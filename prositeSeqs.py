########################################################
# To run this program you MUST have the following files:
# 'trimmedProteins.fasta' - Trimmed fasta file
# 'prosite.dat' - Prosite regular expression database file
# psscan must be specified in path and ps_scan must be executable
########################################################
import os

#hundred and one dalmati- I mean - protein sequences
t_Prot = 'trimmedProteins.fasta'

database = 'prosite.dat'

outfile = 'prositeOut.txt'

#scan the database with the protein sequences
print 'Scanning prosite database with protein sequences\n\n'
scan = './ps_scan.pl -d ' + database + ' ' +  t_Prot + ' > ' + outfile
os.system(scan)
