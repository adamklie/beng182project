########################################################
# To Run this program you MUST have the following files:
# 'blastOut.xml' - Blast output in parsing format
# Parses blast output and returns dictionary of protein
# IDs as keys and keywords as values
# The first keyword is the main title of the best hit
# from blast (E-VALUE < 1) followed by @ seperated
# keywords pulled from ncbi
########################################################

from Bio import SearchIO

def parsePfam():
	accessions = {}
	output = {}
	for qresult in SearchIO.parse('./output/pfamOut.txt', 'hmmer3-tab'):
		keywords = []
		queryID = qresult.id.split(':')[1]
		for item in qresult.hits:
			if item.evalue < 1.0:
	  			keywords.append(item.description)
				accessions.setdefault(queryID, []).append(item.accession.split('.')[0])
		keywordsWeWant = ""
		for keyword in keywords:
			keywordsWeWant += '; ' + keyword
		keywordsWeWant = keywordsWeWant[2:]
		output[queryID] = keywordsWeWant
	return (output, accessions)
