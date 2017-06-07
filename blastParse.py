########################################################
# To Run this program you MUST have the following files:
# 'blastOut.xml' - Blast output in parsing format

# Parses blast output and returns dictionary of protein
# IDs as keys and keywords as values
# The first keyword is the main title of the best hit
# from blast (E-VALUE < 1) followed by @ seperated
# keywords pulled from ncbi
########################################################

from Bio.Blast import NCBIXML
from Bio import SwissProt
from Bio import ExPASy

def parseBlast():
	result_handle = open("./output/blastOut.xml")
	blast_records = NCBIXML.parse(result_handle)
	E_VALUE_THRESH = 1
	blastHits = {}
	accessions = {}
	#Loop through each protein query results
	for blast_record in blast_records:
		keyword_list = []	#stores running keyword list
		queryID = blast_record.query.split()[0].split(':')[1]	#parse for the query protein ID
		#Loop through the hits associated with particular sequence
		for alignment in blast_record.alignments:
			for hsp in alignment.hsps:
				#Hit must have e-value < threshold to be considered
				if hsp.expect < E_VALUE_THRESH:
					title = alignment.title	#title of hit
					splittitle = title.split()
					raw_protein_title = title.split('OS')[0]	#specific keywords in title
					protein_title = " ".join(raw_protein_title.split()[2:])
					keyword_list.append(protein_title)
					accession = splittitle[1].split('|')[1] #parse for the accession number
					accessions.setdefault(queryID, []).append(accession)	
					#print(queryID,":")
					#print(accession)
					handle = ExPASy.get_sprot_raw(accession)
					record = SwissProt.read(handle)	
					keyword_list += record.keywords
					keyword_string = '; '.join(keyword_list)
					blastHits[queryID] = keyword_string
			break	#only take top hit for now
	return (blastHits, accessions)
