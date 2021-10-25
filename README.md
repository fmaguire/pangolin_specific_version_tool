# Tool to install a specific set of pangolin dependency versions

Simple script to support upgrading/downgrading a [pangolin](https://github.com/cov-lineages/pangolin) 
install to a specific version of pangolin with specific dependency versions (e.g., [assignment models](https://github.com/pangoLEARN), 
[scorpio](https://gitub.com/cov-lineages/scorpio), 
[constellations](https://github.com/cov-lineages/constellations), 
and aliases from [pango-designation](https://github.com/cov-lineages/pango-designation)).

This script takes a set of versions in a file and uses to pip to 
upgrade/downgrade the pangolin install in the working environment 
(e.g., conda environment) to match those versions.

Requirements: pangolin install, pip, internet connectivity to [github](https://github.com).

## Example input

An example input (could be copy and pasted into a text file from the PHO 
bioinformatics working group email) contains dependencies and required versions in the format of "Tool: VERSION".
This doesn't have to include all dependencies if not all need pinned to a specific version.

`example_input.txt` contains:
```
pangolin: v3.1.14
pangolearn: 2021-10-13
constellations: v0.0.18
scorpio: v0.3.13
pango-designation: v1.2.88
```

## Example Usage

Assuming your pangolin install is in a conda environment called "pangolin" and
this is being run on a system with internet access.

```
conda activate pangolin
python install_specific_pangolin_versions.py --versions_file example_input.txt
```

This will output the currently installed verions followed by the versions
that have been installed by the script (this should match the versions in the
input file).