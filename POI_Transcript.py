#!/usr/bin/python

import os
import sys

Ctl=['Ctl-HA-1.exon','Ctl-HA-2.exon','GFP-HA-1.exon','GFP-HA-2.exon','GFP-HA-3.exon']
Ctllist=[]
Genes={}
Keys={}
Outnames={}
infile = open('result_T5/EnrichmentTranscripts/Gene_TranscriptsBased','r')
for line in infile.xreadlines():
  array = line.rstrip().rsplit('\t')
  if 'Ctl-' in line: 
    for i in range(1,len(array)):
      if array[i] not in Ctl:
        key = array[i].rsplit('-')[0]
        if not Genes.has_key(key):
          Genes[key]={}
          outfile=open('result_T5/EnrichmentTranscripts/'+key+'_POI-NS1','w')
          Outnames[key]=outfile
        Keys[i]=key
      else:
        Ctllist.append(i)
    outfile.write('\n')
    continue
  Ctls=[]
  for i in Ctllist:
    Ctls.append(float(array[i]))
  for i in Keys.keys():
    if not Genes[Keys[i]].has_key(array[0]):
      Genes[Keys[i]][array[0]]=[float(array[i])]
    else:
      Genes[Keys[i]][array[0]].append(float(array[i]))
  for gene in Genes.keys():
    if not 'NS1' in gene: continue
    if max(Ctl)<2 and min(Genes[gene][array[0]])>1: #Cutoff tunable
        Outnames[gene].write(array[0]+'\t'+'\t'.join(map(str,Genes[gene][array[0]]))+'\n')
infile.close()
     
    
