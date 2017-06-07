########################################################
# To Run this program you MUST have the following files:
# 'fastaSeq.fasta' - Original, large fasta file
# 
# Protein sequences output to 'trimmedProteins.fasta'
########################################################
import os
import re

def trimProteins():
	numCarrots = 0 
	gene_ids = {}
	readFile = open('fastaSeq.fasta', 'r')
	outputFile = open('trimmedProteins.fasta', 'w')
	for line in readFile:
		if line[0] == '>':
			numCarrots += 1
			if numCarrots >= 450 and numCarrots <= 549:
				outputFile.write(line)
				splitline = line.split()
				GNs = re.findall('GN=........', line)
				GN = GNs[0].split('=')[1]
				splitline2 = splitline[0].split(':')
				queryID = splitline2[1]
				gene_ids[queryID] = GN
			elif numCarrots > 549:
				break 
		elif numCarrots >= 450 and numCarrots <= 549:
			outputFile.write(line)
	return gene_ids
#print(trimProteins())
