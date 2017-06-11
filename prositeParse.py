###################################################
# Function to parse prosite output
###################################################

def parseProsite():
	handle = open("./output/prositeOut.txt")
	prositeHits = {}
	accessions = {}
	for line in handle.readlines():
		if line[0] == '>':
			splitline = line.split(':')
			queryID = splitline[1]
			queryID = queryID.rstrip()
			queryID = queryID.lstrip()
			doubleSplitline = splitline[2]
			accession = doubleSplitline.split()[0]
			accessions.setdefault(queryID,[]).append(accession)
			keywords = " ".join(doubleSplitline.split()[2:]).rstrip('.')
			prositeHits.setdefault(queryID, "")
			prositeHits[queryID] += '; ' + keywords
	for key in prositeHits:
		prositeHits[key] = prositeHits[key][2:]
	return (prositeHits, accessions)
