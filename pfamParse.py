########################################################
# Function to parse hmmscan tabular output for keywords
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
