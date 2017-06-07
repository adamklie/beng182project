from bioservices.kegg import KEGG
from readFasta import trimProteins

print('')
print('Reading and trimming the fasta\n')
gene_ids = trimProteins()

import blastSeqs
import pfamSeqs
import prositeSeqs

from blastParse import parseBlast
from pfamParse import parsePfam
from prositeParse import parseProsite
from blast2GOParse import parseBlastGO
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
blast2GO = parseBlastGO('./go/blast2go')
pfam2GO = parsePfamGO('./go/pfam2go')
prosite2GO = parsePrositeGO('./go/prosite2go')

print('Outputting to tsv\n')
output = open('./output/table.tsv', 'w')
header = 'reference\tBLAST\tPfam\tProsite\tKEGG Pathway\tGene Ontology\tComments\n'
output.write(header)

for ids in gene_ids:
	#Get GO terms and IDs
	GO_IDs = ''
	if blastAccessions.get(ids) != None:
		for accession in blastAccessions[ids]:
			if blast2GO.get(accession) != None:
				GO_IDs += blast2GO[accession] + '; '
	if pfamAccessions.get(ids) != None:
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
	if len(GO_IDs) == 0:
		GO_IDs = 'NULL'
	
	# Make sure there are blast hits
	if blastHits.get(ids) != None:
		blast_text = blastHits[ids]
        else:
		blast_text = ''

	if pfamHits.get(ids) != None:
		pfam_text = pfamHits[ids]
	else:
		pfam_text = 'NULL'

	if prositeHits.get(ids) != None:
		prosite_text = prositeHits[ids]
	else:
		prosite_text = 'NULL'

	# Get the KEGG hits
	kegg = KEGG()
	kegg_text = ''
	gene_id = gene_ids[ids]
	KEGG_IDs = kegg.get_pathway_by_gene(gene_id, "acb")
	if KEGG_IDs != None:
		for KEGG_ID in KEGG_IDs:
			kegg_text += KEGG_IDs[KEGG_ID] + ' [' + KEGG_ID + ']; '
		kegg_text = kegg_text[:-2]
	else:
		kegg_text = 'NULL'
	comments = 'NULL'
			
	row = ids + '\t' + blast_text + '\t' + pfam_text + '\t' + prosite_text + '\t' + kegg_text + '\t' + GO_IDs + '\t' + comments + '\n'
	output.write(row)
	
	

