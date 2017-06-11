########################################################
# To Run this program you MUST have the following files:
# 'uniprot-all.fasta' - Uniprot Database File
########################################################

import os

#Get the trimmed protein sequences
protSeq = 'trimmedProteins.fasta'

#Blasting swissprot/uniprot db against the trimmed protein sequence through swissprot db
print 'Preparing Blast Database\n'
uniprotDb = './databases/uniprot-all.fasta' 
#preps the blast search by making a blast db
makeBlast  = 'makeblastdb -in ' +  uniprotDb + ' -dbtype prot'
#os.system(makeBlast)	#uncomment if you do not already have database prepped

#Querys the blast db to pull out hits, stored in blastOut
print 'Running Blast Queries\n'
blastOut1 = './output/blastOut.xml'	#plain text file for readability
blastOut2 = './output/blastOut.txt'	#xml file for parsing
queryBlastXML = 'blastp -query ' + protSeq + ' -db ' + uniprotDb + ' -outfmt 5 ' + ' > ' + blastOut1
queryBlastTXT = 'blastp -query ' + protSeq + ' -db ' + uniprotDb + ' > ' + blastOut2
os.system(queryBlastXML)
os.system(queryBlastTXT)
