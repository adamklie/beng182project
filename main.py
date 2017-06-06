import blastSeqs
import pfamSeqs
import prositeSeqs
from blastParse import parseBlast
from pfamParse import parsePfam
from prositeParse import parseProsite
from pfam2GOParse import parsePfamGO
from prosite2GOParse import parsePrositeGO

print('Parsing\n')
blast = parseBlast()
pfam = parsePfam()
prosite = parseProsite()

blastHits = blast[0]
pfamHits = pfam[0]
prositeHits = prosite[0]
blastAccessions = blast[1]
pfamAccessions = pfam[1]
prositeAccessions = prosite[1]
print('Setting up maps to GO terms\n')
pfam2GO = parsePfamGO('./go/pfam2go')
prosite2GO = parsePrositeGO('./go/prosite2go')

print('Outputting to tsv\n')
output = open('./output/table.tsv', 'w')
#header = 'reference\tBLAST\tPfam\tProsite\tuniprot\tGO\tComments\n'

for ids in blastHits:
	GO_IDs = ''
	for accession in pfamAccessions[ids]:
		if pfam2GO.get(accession) != None:
			for go_id in pfam2GO[accession]:
				GO_IDs += go_id + '; '
        if prositeAccessions.get(ids) != None:
		for accession in prositeAccessions[ids]:
			if prosite2GO.get(accession) != None:
				for go_id in prosite2GO[accession]:	
					GO_IDs += go_id + '; '
	GO_IDs = GO_IDs[:-2]
	blast_text = blastHits[ids]
	if pfamHits.get(ids) != None:
		pfam_text = pfamHits[ids]
	else:
		pfam_text = ''
	if prositeHits.get(ids) != None:
		prosite_text = prositeHits[ids]
	else:
		prosite_text = ''
	uniprotIDs = ''
	for uniprotID in blastAccessions[ids]:
		uniprotIDs += uniprotID + '; '
	uniprotIDs = uniprotIDs[:-2]
	row = ids + '\t' + blast_text + '\t' + pfam_text + '\t' + prosite_text + '\t' + uniprotIDs + '\t' + GO_IDs + '\t' + '\n'
	output.write(row)
	
	

