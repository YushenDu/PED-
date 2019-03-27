#!/usr/bin/python

import os
import sys

Enrichment= {}
Enrichment2 = {}
pop=[]
Muts=[]
Muts2=[]
infile = open('CompareInput/CombineFile_Input_Exon','r')
for line in infile.readlines():
  array = line.rstrip().rsplit('\t')
  if 'StarPos' in line: 
    print len(array)
    for item in range(8,len(array)):
      pop.append(array[item])
      Enrichment[array[item]]={}
    continue
  else:
    mut = '*'.join([array[0],array[3],array[4],array[5]])
    Muts.append(mut)
    for i in range(8,len(array)):
      if Enrichment[pop[i-8]].has_key(mut):
        Enrichment[pop[i-8]][mut].append(float(array[i]))
      else:
        Enrichment[pop[i-8]][mut] = []
        Enrichment[pop[i-8]][mut].append(float(array[i]))
print pop
infile.close()

Muts= set(Muts)
Muts= list(Muts)
print len(Muts)


outfile = open('CompareInput/CombineFile_Input_TranscriptSum','w')
outfile.write('Chr'+'\t'+'gene_id'+'\t'+'transcript_id'+'\t'+'transcript_name'+'\t')
for p in pop:
  outfile.write(p+'\t')
outfile.write('\n')

for mut in Muts:
  outfile.write('\t'.join(mut.rsplit('*'))+'\t')
  for p in pop:
    outfile.write(str(sum(Enrichment[p][mut]))+'\t')
  outfile.write('\n')
outfile.close()
