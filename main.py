import blastSeqs
import pfamSeqs
import prositeSeqs
from blastParse import parseBlast
from pfamParse import parsePfam
from prositeParse import parseProsite

blastSeqs
pfamSeqs
prositeSeqs
blastHits = parseBlast()
pfamHits = parsePfam()
prositeHits = parseProsite()

output = open('./output/table.tsv', 'w')
header = 'reference\tBLAST\tPfam\Prosite\tKEGG Pathway\tGene Ontology\tComments\n'
output.write(header)
for ids in blastHits:
	row = ids + '\t' + blastHits[ids] + '\t' + pfamHits[ids] + '\t' + prositeHits[ids] + '\n'
	output.write(row)
	
	

