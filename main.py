import blastSeqs
import pfamSeqs
import prositeSeqs
from blastParse import parseBlast
from pfamParse import parsePfam
from prositeParse import parseProsite
from pfam2GOParse import parsePfamGO
from prosite2GOParse import parsePrositeGO

print('Parsing blast')
blast = parseBlast()
print('Parsing pfam')
pfam = parsePfam()
print('Parsing prosite')
prosite = parseProsite()

blastHits = blast[0]
pfamHits = pfam[0]
prositeHits = prosite[0]

blastAccessions = blast[1]
pfamAccessions = pfam[1]
prositeAccessions = prosite[1]

print('Setting up maps to GO terms')
pfam2GO = parsePfamGO('./go/pfam2go')
prosite2GO = parsePrositeGO('./go/prosite2go')

print('Outputting to tsv')
output = open('./output/table.tsv', 'w')
#header = 'reference\tBLAST\tPfam\tProsite\tuniprot\tGO\tComments\n'

for ids in blastHits:
	GO_IDs = ''
	for accession in pfamAccessions[ids]:
		if pfam2GO.get(accession) != None:
			for go_id in pfam2GO[accession]:
				GO_IDs += go_id + '; '
        for accession in prositeAccessions[ids]:
		if prosite2GO.get(accession) != None:
			for go_id in prosite2GO[accession]:	
				GO_IDs += go_id + '; '
	GO_IDs = GO_IDs[:-2]
	row = ids + '\t' + blastHits[ids] + '\t' + pfamHits[ids] + '\t' + prositeHits[ids] + '\t' + blastAccessions[ids][0] + '\t' + GO_IDs + '\t' + '\n'
	output.write(row)
	
	

