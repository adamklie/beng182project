#######################################################
# To Run this program you MUST have the following files:
# 'fastaSeq.fasta' - Original, large fasta file
# 'readFasta.py' - Trims out 101 protein sequences
# 'uniprot-all.fasta' - Uniprot Database File
########################################################
import os

#Original fasta protein sequence
originalFasta = 'fastaSeq.fasta'

#Make a trimmed version of the original fasta file called trimmedProteins.fasta
print ''
print 'Trimming protein sequence \n' 
os.system('python readFasta.py' )
protSeq = 'trimmedProteins.fasta'

#installs Blast
#os.system('brew install blast')

#Blasting swissprot db against the trimmed 101 protein sequence through swissprot db
print ''
print 'Preparing Blast Database\n'
uniprotDb = 'uniprot-all.fasta' 
#preps the blast search by making a blast db
makeBlast  = 'makeblastdb -in ' +  uniprotDb + ' -dbtype prot'
#os.system(makeBlast)

#Querys the blast db to pull out hits, stored in blastOut
print ''
print 'Running Blast Queries'
blastOut1 = 'blastOut.xml'
blastOut2 = 'blastOut.txt'
queryBlastXML = 'blastp -query ' + protSeq + ' -db ' + uniprotDb + ' -outfmt 5 ' + ' > ' + blastOut1
queryBlastTXT = 'blastp -query ' + protSeq + ' -db ' + uniprotDb + ' > ' + blastOut2
os.system(queryBlastXML)
os.system(queryBlastTXT)
