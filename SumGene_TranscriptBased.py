#!/usr/bin/python

import os
import sys

Enrichment= {}
pop=[]
Muts=[]
infile = open('result_T4/EnrichmentTranscripts/Enrichment_Transcripts','r')
for line in infile.xreadlines():
  array = line.rstrip().rsplit('\t')
  if 'gene_id' in line: 
    for item in range(4,len(array)):
      pop.append(array[item])
      Enrichment[array[item]]={}
#    print pop
    continue
  else:
    mut = array[3].rsplit('"')[-2].rsplit('-')[0] #Gene
    Muts.append(mut)
    for i in range(4,len(array)):
      if Enrichment[pop[i-4]].has_key(mut):
        Enrichment[pop[i-4]][mut].append(float(array[i]))
      else:
        Enrichment[pop[i-4]][mut] = []
        Enrichment[pop[i-4]][mut].append(float(array[i]))

#    print mut
infile.close()

Muts= set(Muts)
Muts= list(Muts)
print len(Muts)

outfile = open('result_T4/EnrichmentTranscripts/Gene_TranscriptsBased','w')
outfile.write('Gene'+'\t')
for p in pop:
  outfile.write(p+'\t')
outfile.write('\n')

for mut in Muts:
  outfile.write('\t'.join(mut.rsplit('*'))+'\t')
  for p in pop:
    outfile.write(str(max(Enrichment[p][mut]))+'\t')
  outfile.write('\n')
outfile.close()
