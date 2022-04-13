#!/usr/bin/env python

import sys
import argparse
import subprocess

"""
pangolin: 4.0
pangolin-data: 1.2.133
constellations: 0.0.18
scorpio: 0.3.13
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Modify pangolin in conda env "
                                                 "to specific versions using "
                                                 "pip")
    parser.add_argument("--versions_file", required=True, type=str,
                        help="File containing pangolin dependency "
                                    "versions e.g., \npangolin: 3.1.14"
                                    "\npangolearn: 2021-10-13"
                                    "\n...")
    args = parser.parse_args()

    # provides current pangolin install details
    # and load them in a dict for comparison
    print("## Existing pangolin install:")
    installed_versions = subprocess.run(["pangolin", "--all-versions"],
                                        check=True,
                                        stdout=subprocess.PIPE)

    installed_versions = installed_versions.stdout.decode('utf-8')
    print(installed_versions)
    installed_ver_dict = {}
    for dep_ver in map(str.strip, installed_versions.split('\n')):
        # skip empty line at end
        if len(dep_ver) == 0:
            continue

        dependency, version = dep_ver.split(': ')
        if not version.startswith("v"):
            version = "v" + version
        installed_ver_dict[dependency] = version

    # parse the dependency version file provided, validate real dependencies
    # tidy up version strings, and then use pip to update
    valid_deps = ['pangolin', 'pangolin-data', 'constellations',
                  'scorpio']
    print("## Changing installed versions as needed:")
    versions = {}
    with open(args.versions_file) as fh:
        for line in fh:
            line = line.split(':')
            dependency = line[0].strip()
            dependency = dependency.replace(" ", "-").lower()
            version = line[1].strip()

            # check for invalid deps
            if dependency not in valid_deps:
                raise ValueError(f"{dependency} is not a valid pangolin "
                                 f"dependency. Must be in {valid_deps}")

            # tidy up strings
            if not version.startswith("v"):
                version = "v" + version

            installed_version = installed_ver_dict[dependency]
            if version == installed_version:
                print(f"{dependency} not updated as requested {version} already installed")
            else:
                print(f"Changing {dependency} from {installed_version} to {version}")
                subprocess.run([sys.executable, '-m', 'pip', 'install',
                                f"git+https://github.com/cov-lineages/{dependency}.git@{version}"],
                                check=True,
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)

    # provides pangolin install details after update to specific versions in
    # supplied version file
    print("\n## Pangolin and dependencies now:")
    subprocess.run(["pangolin", "--all-versions"], check=True)
