###################################################

###################################################

def parseProsite():
	handle = open("./output/prositeOut.txt")
	prositeHits = {}
	for line in handle.readlines():
		if line[0] == '>':
			splitline = line.split(':')
			queryID = splitline[1]
			queryID = queryID.rstrip()
			queryID = queryID.lstrip()
			keywords = " ".join(splitline[2].split()[2:]).rstrip('.')
			prositeHits.setdefault(queryID, "")
			prositeHits[queryID] += '@' + keywords
	for key in prositeHits:
		prositeHits[key] = prositeHits[key][1:]
	return prositeHits
