# blue-carbon-microbiomes
Analysis of blue carbon microbiomes 
# Getting started
## Creating a manifest file
Since the data has already been demultiplexed we will provide a [manifest file](https://docs.qiime2.org/2021.8/tutorials/importing/#fastq-manifest-formats) to import  the sequence reads. A manifest is similar to an experiment metadata file and can both be validated using the [Keemei](https://keemei.qiime2.org/) google sheets extension and error messages appear to refer to use "metadata" when referring to the manifest file when importing data.

Given the number of files, it is best to build the manifest using the script. I have created a [simple script](scripts/qiime_buildmanifest.py) for this purpose, this script is not extensively tested, so the output must be visually inspected. Download the script to your working directory and then provide it with the path to reads and the path where the manifest will be written to. We can then just run the script as follows:

```
python qiime_buildmanifest.py \
    -r /home/andhlovu/atacama_data/testdata \
    -m /home/andhlovu/metavars/atacama_manifest.tsv
```
## import reads into [QIIME](https://qiime2.org/)

Once we have a manifest file we can import our reads into QIIME

```
module load app/QIIME/2022.11

output_dir=/home/andhlovu/Atacama_soil
raw_reads=/home/andhlovu/atacama_data

qiime tools import \
   --type 'SampleData[PairedEndSequencesWithQuality]' \
   --input-path /home/andhlovu/metavars/atacama_manifest.tsv \
   --output-path ${output_dir}/raw_reads/emp-paired-end-sequences.qza \
   --input-format PairedEndFastqManifestPhred33V2

```
## Denoising and Sequence quality control with [DADA](https://benjjneb.github.io/dada2/)
We skip the de-multiplexing steps and jump to denoising in the Qiime workflow. Here we are using thresholds from the Atacama tutorial, these must be chosen following analysis of the quality of the data and therefore this step may have to be repeated until good quality data is produced.

```
mkdir ${output_dir}/dada
qiime dada2 denoise-paired \
  --i-demultiplexed-seqs  ${output_dir}/raw_reads/emp-paired-end-sequences.qza \
  --p-trim-left-f 13 \
  --p-trim-left-r 13 \
  --p-trunc-len-f 150 \
  --p-trunc-len-r 150 \
  --o-table ${output_dir}/dada/table.qza \
  --o-representative-sequences ${output_dir}/dada/rep-seqs.qza \
  --o-denoising-stats ${output_dir}/dada/denoising-stats.qza

````
