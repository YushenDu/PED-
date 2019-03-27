#!/usr/bin/python

import os
import sys

Enrichment={}
Pop=[]
Muts=[]
infile = open('result_T5/CombineFile_Exon','r')
outfile1 = open('result_T5/Enrichment_Exon','w')
for line in infile.xreadlines():
  array = line.rstrip().rsplit('\t')
  if 'StarPos' in line:
    for item in array[8::]:
      Enrichment[item]={}
      Pop.append(item)
    outfile1.write('\t'.join(array[0:8])+'\t'+'\t'.join(Pop_HA)+'\n')
    continue
#  print array
#  sys.exit()
  Input1 = float(array[15])
  Input2 = float(array[16])
  
  key='*'.join(array[0:8])
  Muts.append(key)
  for i in range(8,len(array)):
    if ('-1' in Pop[i-8] or '-2' in Pop[i-8]) and Input1>0.1:
      Enrichment[Pop[i-8]][key]=float(array[i])/Input1
    elif ('-3' in Pop[i-8] or '-4' in Pop[i-8] or '-5' in Pop[i-8]) and Input2>0.1:
      Enrichment[Pop[i-8]][key]=float(array[i])/Input2
    else:
      Enrichment[Pop[i-8]][key]=0
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

 

      
      
  
  
