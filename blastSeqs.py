########################################################
# To Run this program you MUST have the following files:
# 'fastaSeq.fasta' - Original, large fasta file
# 'readFasta.py' - Trims out 101 protein sequences
# 'uniprot-all.fasta' - Uniprot Database File
########################################################
import os

#Original fasta protein sequence
originalFasta = 'fastaSeq.fasta'

#Get the trimmed protein sequences
protSeq = 'trimmedProteins.fasta'

#installs Blast, assumed to be installed
#os.system('brew install blast')

#Blasting swissprot/uniprot db against the trimmed protein sequence through swissprot db
print ''
print 'Preparing Blast Database\n'
uniprotDb = './databases/uniprot-all.fasta' 
#preps the blast search by making a blast db
makeBlast  = 'makeblastdb -in ' +  uniprotDb + ' -dbtype prot'
#os.system(makeBlast)

#Querys the blast db to pull out hits, stored in blastOut
print 'Running Blast Queries\n'
blastOut1 = './output/blastOut.xml'	#plain text file for readability
blastOut2 = './output/blastOut.txt'	#xml file for parsing
queryBlastXML = 'blastp -query ' + protSeq + ' -db ' + uniprotDb + ' -outfmt 5 ' + ' > ' + blastOut1
queryBlastTXT = 'blastp -query ' + protSeq + ' -db ' + uniprotDb + ' > ' + blastOut2
os.system(queryBlastXML)
os.system(queryBlastTXT)
