#!/usr/bin/python

import os
import sys

Enrichment={}
Pop=[]
Muts=[]
infile = open('result_T4/EnrichmentTranscripts/TranscriptSum','r')
outfile1 = open('result_T4/EnrichmentTranscripts/Enrichment_Transcripts','w')
for line in infile.xreadlines():
  array = line.rstrip().rsplit('\t')
  if 'Ctl' in line:
    for item in array[4::]:
      Enrichment[item]={}
      Pop.append(item)
    outfile1.write('\t'.join(array[0:4])+'\t'+'\t'.join(Pop)+'\n')
    continue
  Input = float(array[7])
  key='*'.join(array[0:4])
  Muts.append(key)
  for i in range(4,len(array)):
    if Input>0.1:
      Enrichment[Pop[i-4]][key]=float(array[i])/Input
    else:
      Enrichment[Pop[i-4]][key]=0
infile.close()


Muts= set(Muts)
Muts= list(Muts)
print len(Muts)

for m in Muts:
  key=m.rsplit('*')
  outfile1.write('\t'.join(key)+'\t')
  for p in Pop:
    outfile1.write(str(Enrichment[p][m])+'\t')
  outfile1.write('\n')
outfile1.close()
 

      
      
  
  
