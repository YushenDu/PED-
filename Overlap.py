#!/usr/bin/python
import os
import sys
import glob
Exon=[]
infile = open('result_T5/EnrichmentExon/NS1_Exon.POI','r')
for line in infile.xreadlines():
  array = line.strip().rsplit('\t')
  Exon.append(array[0])
infile.close()

filenames = glob.glob('result_T5/EnrichmentTranscript/NS1*')
for filename in filenames:
  print filename 
  infile = open(filename,'r')
  outfile= open(filename+'_POI','w')
  for line in infile.xreadlines():
    array = line.rstrip().rsplit('\t')
    if not array[0] in Exon:
      outfile.write(line)
infile.close()
outfile.close()
