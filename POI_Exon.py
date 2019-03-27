#!/usr/bin/python

import os
import sys

Ctl=['Ctl-HA-1.exon','Ctl-HA-2.exon','GFP-HA-1.exon','GFP-HA-2.exon','GFP-HA-3.exon']
Ctllist=[]
Genes={}
Keys={}
Outnames={}
infile = open('result_T5/EnrichmentExon/Gene_Exon','r')
for line in infile.xreadlines():
  array = line.rstrip().rsplit('\t')
  if 'NS1-' in line: 
    for i in range(2,len(array)):
      if array[i] not in Ctl:
        key = array[i].rsplit('-')[0]
        if not Genes.has_key(key):
          Genes[key]={}
          outfile=open('result_T5/EnrichmentExon/'+key+'.POI-NS1','w')
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
    print Keys[i],array[1]
    
    if Genes[Keys[i]].has_key(array[1]):
      Genes[Keys[i]][array[1]].append(float(array[i]))
    else:
      Genes[Keys[i]][array[1]]=[float(array[i])]
  for gene in Genes.keys():
#    if min(Genes[gene][array[1]])> 3 and max(Genes[gene][array[1]])>10 and sum(Genes[gene][array[1]])/len(Genes[gene][array[1]])>5:
    if min(Genes[gene][array[1]])> 2 and max(Ctl)<2 :# Cutoff adjustable
      Outnames[gene].write(array[1]+'\t'+'\t'.join(map(str,Genes[gene][array[1]]))+'\n')
infile.close()
     
    
