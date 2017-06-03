from Bio import SearchIO
output = {}
for qresult in SearchIO.parse('hmmscan_out.txt', 'hmmer3-tab'):
	keywords = []
	queryID = qresult.id.split(':')[1]
	for item in qresult.hits:
		if item.evalue < 1.0:
	  		keywords.append(item.description)
	keywordsWeWant = ""
	for keyword in keywords:
		keywordsWeWant += '@' + keyword
	keywordsWeWant = keywordsWeWant[1:]
	output[queryID] = keywordsWeWant
	print(output)

