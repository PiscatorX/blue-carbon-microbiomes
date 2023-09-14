#!/usr/bin/env python
from argparse import RawTextHelpFormatter
import os
import sys
import glob
import pprint
import argparse

def build_manifest(read_dir, spliton, manifest):

    search_dir = os.path.join(read_dir,"*.f*q*")
    read_files  =  list(map(os.path.abspath, sorted(glob.glob(search_dir))))

    if not read_files:raise Exception("No reads found check read directory path. Do the read extensions match the pattern '*.f*q*' ")
    
    label  = lambda fname:  os.path.basename(fname.rsplit(spliton, 1)[0])
    n = len(read_files) 
    if n%2 != 0:
        raise Exception("Uneven number of read, reads should paired")

    
    file_pairs = dict( (label(read_files[i]), read_files[i:i+2]) for i in range(0, n, 2))
    
    with open(manifest, 'w') as manifest_fp:
        print("sample-id\tforward-absolute-filepath\treverse-absolute-filepath", file = manifest_fp)
        for tag, reads in file_pairs.items():
            tsv_line = "{}\t{}\t{}".format(tag, reads[0],reads[1])
            print(tsv_line, file = manifest_fp)
            
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Generates a qiime manifest file for paired-end data https://docs.qiime2.org/2021.8/tutorials/importing/#fastq-manifest-formats \nAssumes that reads have have the '*.fastq' | *.fq | '*.fastqz' extension.", formatter_class=RawTextHelpFormatter)

    parser.add_argument('-r','--read-dir', dest='read_dir',
                        action='store', required=True, type=str)
    parser.add_argument('-s','--spliton', dest='spliton', default="_", help ="For sample name detection. The character in all read filename immediately before readnumber. e.g for 'RemovePrimer_Final.LB6_1.fq.gz' spliton = '_'",
                        action='store', required=False, type=str)
    parser.add_argument('-m','--manifest-file', dest='manifest',
                        action='store', required=True, type=str)
    
    args = parser.parse_args()
    
    build_manifest(args.read_dir, args.spliton, args.manifest)
