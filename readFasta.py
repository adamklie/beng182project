########################################################
# To Run this program you MUST have the following files:
# 'fastaSeq.fasta' - Original, large fasta file
# 
# Protein sequences output to 'trimmedProteins.fasta'
########################################################
import os
numCarrots = 0 
readFile = open('fastaSeq.fasta', 'r')
outputFile = open('trimmedProteins.fasta', 'w')
for line in readFile:
	if line[0] == '>':
		numCarrots += 1
		if numCarrots >=  450 and numCarrots <= 454:
			outputFile.write(line)
		elif numCarrots >  550:
			break 
	elif numCarrots >=  450 and numCarrots <= 454:
		outputFile.write(line)
