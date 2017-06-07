def parseBlastGO(filename):
	goFile = open(filename,'r')
	goDict = {}
	goFile.readline()
	for line in goFile:
		ln = line.strip().split('\t')
		if len(ln) > 1:
			goDict[ln[0]] = ln[1]
			#print ln[0], ln[1]
	#print(goDict)
	return goDict
