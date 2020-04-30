import csv
import argparse
import re
from Bio import SeqIO
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("gff")
parser.add_argument("fasta")
args = parser.parse_args()
watermelon = SeqIO.read(args.fasta, "fasta")
first_dict = defaultdict(dict)
with open(args.gff, "r") as gff_file:
	reader = csv.reader(gff_file, delimiter="\t")
	for line in reader:
		if not line:
			continue
		else:
			organism = line[0].replace(" ", "_")
			start_coordinate = int(line[3])
			end_coordinate = int(line[4])
			feature = line[2]
			strand = line[6]
			form = line[8]
			if feature == "CDS":
				sequence = watermelon.seq[start_coordinate-1:end_coordinate]
				if strand == '-':
					sequence = sequence.reverse_complement
				match = re.search("Gene\s+(\S+)\s+", form)
				gene_name = match.group(1)
				another_match = re.search("exon\s+(\d+)", form)
				if another_match:
					exon_number = another_match.group(1)
					first_dict[gene_name][exon_number] = sequence
				else:
					print(">" + organism + "_" + gene_name)
					print(sequence)

for gene, x in first_dict.items():
	print(">" + organism + "_" + gene)
	for exon, y in (first_dict[gene].items()):
		print(y)
	print()
