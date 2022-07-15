# Tool to install a specific set of pangolin dependency versions

**NOTE: current version of tool only works for pangolin >= 4.0**
If you want/need support across major pangolin releases feel free to submit a PR!

Simple script to support upgrading/downgrading a [pangolin](https://github.com/cov-lineages/pangolin) v4
install to a specific version of pangolin with specific dependency versions (e.g., [assignment models](https://github.com/cov-lineages/pangoLEARN), 
[scorpio](https://github.com/cov-lineages/scorpio), 
[constellations](https://github.com/cov-lineages/constellations), 
and aliases from [pango-designation](https://github.com/cov-lineages/pango-designation)).

This script takes a set of versions in a file and uses to pip to 
upgrade/downgrade the pangolin install in the working environment 
(e.g., conda environment) to match those versions.

**Requirements: pangolin install (includes python and pip) and internet connectivity to [github](https://github.com)**

## Example input

An example input (could be copy and pasted into a text file from the PHO 
bioinformatics working group email) contains dependencies and required versions in the format of "Tool: VERSION".
This doesn't have to include all dependencies if not all need pinned to a specific version.

`example_input.txt` contains:
```
pangolin: 4.1.1
pangolin-data: v1.11
pangolin-assignment: v1.11
scorpio: v0.3.17
constellations: v0.1.10
```

## Example Usage

Assuming your pangolin install is in a conda environment called "pangolin" and
this is being run on a system with internet access to github. 

```
conda activate pangolin
python install_specific_pangolin_versions.py --versions_file example_input.txt
```

This takes 1-2 minutes and will output the currently installed versions followed by the versions
that have been installed by the script (this should match the versions in the
input file):

```
## Existing pangolin install:
pangolin: 4.1.1
pangolin-data: 1.11
constellations: v0.1.10
scorpio: 0.3.17
pangolin-assignment: 1.9
usher 0.5.3
gofasta 1.0.0
minimap2 2.24-r1122

## Changing installed versions as needed:
pangolin not updated as requested v4.1.1 already installed
pangolin-data not updated as requested v1.11 already installed
Changing pangolin-assignment from v1.9 to v1.11
scorpio not updated as requested v0.3.17 already installed
constellations not updated as requested v0.1.10 already installed

## Pangolin and dependencies now:
pangolin: 4.1.1
pangolin-data: 1.11
constellations: v0.1.10
scorpio: 0.3.17
pangolin-assignment: 1.11
usher 0.5.3
gofasta 1.0.0
minimap2 2.24-r1122
```
