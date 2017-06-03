from Bio.Blast import NCBIXML
from Bio import Entrez
Entrez.email = "Your.Name.Here@example.org"
result_handle = open("blastOut.xml")
blast_records = NCBIXML.parse(result_handle)
E_VALUE_THRESH = 1
blastParse = {}
for blast_record in blast_records:
	keyword_list = ''
	queryID = blast_record.query.split()[0].split(':')[1]
	for alignment in blast_record.alignments:
		for hsp in alignment.hsps:
			if hsp.expect < E_VALUE_THRESH:
				title = (alignment.title)
				print(title)
				splittitle = title.split()
				raw_protein = title.split('OS')[0]
				protein_title = " ".join(raw_protein.split()[2:])
				keyword_list += protein_title
				accession = splittitle[1].split('|')[1]
				handle = Entrez.efetch(db="protein", id=accession, rettype="gb", retmode="text")
				lines = []
				for line in handle.readlines():
					lines.append(line)
					keywords=""
				for i in range(len(lines)):
					if "KEYWORD" in lines[i]:
						while "SOURCE" not in lines[i]:
							line2 = lines[i]
							line2 = line2.rstrip()
							line2 = line2.rstrip('.')
							line2 = line2.lstrip()
							keywords += line2
		  					i += 1
				print(accession)
				print(keywords)
				keywords = keywords[12:]
				raw_keyword_list = keywords.split(';')
				for keyword in raw_keyword_list:						
					keyword_list += '@' + keyword	
				blastParse[queryID] = keyword_list
		break	#only take top hit for now
print(blastParse)
