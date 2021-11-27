#!/usr/bin/env python

import sys
import argparse
import subprocess

"""
pangolin: v3.1.14
pangolearn: 2021-10-13
constellations: v0.0.18
scorpio: v0.3.13
pango-designation: v1.2.88
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Update pangolin in conda env "
                                                 "to specific versions using "
                                                 "pip")
    parser.add_argument("--versions_file", required=True, type=str,
                        help="File containing pangolin dependency "
                                    "versions e.g., \npangolin: 3.1.14"
                                    "\npangolearn: 2021-10-13"
                                    "\n...")
    args = parser.parse_args()

    # provides current pangolin install details
    print("## Current pangolin install:")
    subprocess.run(["pangolin", "--all-versions"], check=True)


    # parse the dependency version file provided, validate real dependencies
    # tidy up version strings, and then use pip to update
    valid_deps = ['pangolin', 'pangolearn', 'constellations',
                  'scorpio', 'pango-designation']
    versions = {}
    with open(args.versions_file) as fh:
        for line in fh:
            line = line.split(':')
            dependency = line[0].strip()
            dependency = dependency.replace(" ", "-").lower()
            version = line[1].strip()

            if dependency not in valid_deps:
                raise ValueError(f"{dependency} is not a valid pangolin "
                                 f"dependency. Must be in {valid_deps}")

            if dependency != "pangolearn" and not version.startswith("v"):
                version = "v" + version

            subprocess.run([sys.executable, '-m', 'pip', 'install',
                            f"git+https://github.com/cov-lineages/{dependency}.git@{version}"],
                            check=True,
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)

    # provides pangolin install details after update to specific versions in
    # supplied version file
    print("\n## Pangolin and dependencies updated to:")
    subprocess.run(["pangolin", "--all-versions"], check=True)
