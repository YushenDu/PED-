# PED
The codes are written to facilitate the analysis of PED data.
The general work flow of the attached scripts are:
CombineBedOut.py takes mapped BED file as input and summarize the RPM of each exon
Then we analyze the enrichment of genes from both exon and gene transcript perspective, following the same procedures.
Exons:
First calculate the enrichment of each exon by comparing with input (CalEnrichemt.py)
Then calculate the enrichment of individual gene by taking the maximum of exon enrichment (SumGene_ExonBased.py)
Then extract the hits (POI_Exon.py)
Transcripts:
First summarize the RPM of each gene transcript by sum up corresponding exons (SumTranscript.py)
Then calculate the enrichment of each gene transcript by comparing with input (CalEnrichemt_Transcript.py)
Then calculate the enrichment of individual gene by taking the maximum of known transcript enrichment (SumGene_TranscriptBased.py)
Then extract the hits (POI_Transcript.py)
Finally, we overlap the hits from exon and gene transcript to get the final lists (Overlap.py). 


CombineBedOut.py
After the sequencing reads are mapped to human genome and then mapped to exon region, we then combine the reads of every sample into a big table for comparison. We also normalized the depth of each exon by RPM.

SumTranscript.py
Summarize the RPMs of individual exons (CDS) into corresponding gene transcripts.

CalEnrichment.py
This script calculate the enrichment of each exon from every pull-down sample comparing with corresponding input. The enrichment is calculated as the RPM (frequency) of each exon divided by the RPM in Input. 

CalEnrichment_Transcript.py
This script calculate the enrichment of each gene transcript from every pull-down sample comparing with corresponding input. The enrichment is calculated as the RPM (frequency) of each gene transcript divided by the RPM in Input. 

SumGene_ExonBased.py
This script calculate the enrichment of each gene as the maximum enrichment of all corresponding exons. 


SumGene_TranscriptBased.py
This script calculate the enrichment of each gene as the maximum enrichment of all corresponding transcript.

POI_Exon.py
Select the enriched genes based on the enrichment score of exons. Current cutoff is minimum of all replicate >2 and control <2. However, this cutoff is adjustable. 

POI_Transcript.py
Select the enriched genes based on the enrichment score of gene transcripts. Current cutoff is minimum of all replicate >1 and control <2. However, this cutoff is adjustable. 

Overlap.py
This final script examined the genes that occurred as hits from both running POI_Exon.py and POI_Transcript.py, as the final hits. 
