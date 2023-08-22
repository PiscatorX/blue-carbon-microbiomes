# blue-carbon-microbiomes
Analysis of blue carbon microbiomes 
# Getting started
## import reads into [QIIME](https://qiime2.org/)
Since the data has already been demultiplexed we will provide a [manifest file](https://docs.qiime2.org/2021.8/tutorials/importing/#fastq-manifest-formats) to import  the sequence reads. A manifest is similar to an experiment metadata file and can both be validated using the [Keemei](https://keemei.qiime2.org/) google sheets extension and error messages appear to refer to use "metadata" when referring to the manifest file when importing data.

Given the number of files, it is best to build the manifest using the script. I have created a [simple script](scripts/qiime_buildmanifest.py) for this purpose, this script is not extensively tested, so the output must be visually inspected. Download the script to your working directory and then provide it with the path to reads and the path where the manifest will be written to (if is a directory it must exist)
