#!/usr/bin/python

import os
import sys
import glob

pop=[]
KEYs={}
filenames = sorted(glob.glob('CompareInput/Exon/*'))
print filenames
for filename in filenames:
  fileID = filename.rsplit('/')[-1]
  pop.append(fileID)
  KEYs[fileID]={}
  infile = open(filename,'r')
  for line in infile.xreadlines():
    array = line.rstrip().rsplit('\t')
#    print array
#    sys.exit()
    k='*'.join(array[0:7])+'*'+array[9]
    KEYs[fileID][k]= array[7]
  infile.close()

Allkey=[]
for k in KEYs:
  Allkey.extend(KEYs[k].keys())
Allkey= list(set(Allkey))

#outfile = 'result_T5/EnrichmentTranscripts/CombineFile_Exon_R1'
outfile = 'CompareInput/CombineFile_Input_Exon'
outfile = open(outfile,'w')
#'chr1	16775588	16778510	gene_id "ENSG00000157191.14"	 transcript_id "ENST00000496239.1"	 transcript_name "NECAP2-003"	 exon_number 5	10	507	2922	0.1735113'
outfile.write('\t'.join(['Chr','StarPos','EndPos','gene_id','transcript_id','transcript_name','exon_number','transcript_length'])+'\t')
for p in pop:
  outfile.write(p+'\t')
outfile.write('\n')

Depth={}
for p in pop:
  Depth[p]=0

for key in Allkey:
  for p in pop:
    if not KEYs[p].has_key(key): continue
    else:
      Depth[p]+=float(KEYs[p][key])
  
print Depth  
for key in Allkey:
  out=key.rsplit('*')
  for p in pop:
#    if not KEYs['Input'].has_key(key): continue
#    if KEYs['Input'][key]<10: continue
    if KEYs[p].has_key(key):
      out.append(str(float(KEYs[p][key])/(Depth[p]+1)*1000000)) # Normalize to per millon
    else:
      out.append(str(0))
  if len(out)>4:
    outfile.write('\t'.join(out))
    outfile.write('\n')
outfile.close()

