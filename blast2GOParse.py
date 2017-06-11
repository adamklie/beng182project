#################################################
# Function that generates mapping between uniprot
# accessions and go terms
#################################################

def parseBlastGO(filename):
	goFile = open(filename,'r')
	goDict = {}
	goFile.readline()
	for line in goFile:
		ln = line.strip().split('\t')
		if len(ln) > 1:
			goDict[ln[0]] = ln[1]
	return goDict
