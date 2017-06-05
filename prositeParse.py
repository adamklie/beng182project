handle = open("prositeOut.txt")
prositeHits = {}
for line in handle.readlines():
	if line[0] == '>':
		splitline = line.split(':')
		queryID = splitline[1]
		queryID = queryID.rstrip()
		queryID = queryID.lstrip()
		keywords = " ".join(splitline[2].split()[2:]).rstrip('.')
		#print(queryID)
		#print(keywords)
		prositeHits.setdefault(queryID, "")
		prositeHits[queryID] += '@' + keywords

for key in prositeHits:
	prositeHits[key] = prositeHits[key][1:]
print(prositeHits)
