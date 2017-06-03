#######################################################
# To Run this program you MUST have the following files:
# 'trimmedProteins.fasta' - Trimmed fasta file
# 'Pfam-A.hmm' - PFAM Database (HMM) File
########################################################
import os

#hundred and one dalmati- I mean - protein sequences
t_Prot = 'trimmedProteins.fasta'

data_Hmm = 'Pfam-A.hmm'

#hmmpress the database
print 'Pressing the HMM database\n\n'
press = 'hmmpress ' + data_Hmm
os.system(press)

#scan the database with the protein sequences
print 'Scanning HMM database with protein sequences\n\n'
scan = 'hmmscan --tblout hmmscan_out.txt -o hmmscan_out.txt ' + data_Hmm + ' ' + t_Prot
os.system(scan)


