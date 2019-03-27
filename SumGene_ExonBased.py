#!/usr/bin/python

import os
import sys

Enrichment= {}
pop=[]
Muts=[]
infile = open('result_T4/Enrichment_Exon','r')
for line in infile.xreadlines():
  array = line.rstrip().rsplit('\t')
  if 'StarPos' in line: 
    print len(array)
    for item in range(8,len(array)):
      pop.append(array[item])
      Enrichment[array[item]]={}
    print pop
    continue
  else:
    mut = array[0]+'*'+array[5].rsplit('"')[-2].rsplit('-')[0]
    Muts.append(mut)
    for i in range(8,len(array)):
      if Enrichment[pop[i-8]].has_key(mut):
        Enrichment[pop[i-8]][mut].append(float(array[i]))
      else:
        Enrichment[pop[i-8]][mut] = []
        Enrichment[pop[i-8]][mut].append(float(array[i]))

#    print mut
infile.close()

Muts= set(Muts)
Muts= list(Muts)
print len(Muts)

outfile = open('result_T4/EnrichmentExon/Gene_Exon','w')
outfile.write('Chr'+'\t'+'gene_name'+'\t')
for p in pop:
  outfile.write(p+'\t')
outfile.write('\n')

for mut in Muts:
  outfile.write('\t'.join(mut.rsplit('*'))+'\t')
  for p in pop:
    outfile.write(str(max(Enrichment[p][mut]))+'\t')
  outfile.write('\n')
outfile.close()
