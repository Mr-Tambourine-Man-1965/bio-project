import csv
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("*.gff")
parser.add_argument("*.fasta")
args = parser.parse_args()
genome = SeqIO.read(args.fasta, "*.fasta")
with open(args.gff, 'r') as gff_file:
	reader = csv.reader(gff_file, delimiter="\t")
	for line in reader:
		columns = line.rstrip("\n").split(",")
		gene = columns[8]
		if gene == gene and not gene.startswith("Gene similar"):
			gene2 = gene[5:9]
			reader2.write(gene2 + "\n")
		else:
			pass
	reader2.close()
	
	sorted_list = sorted(reader2)
	for line in sorted_list:
		alphabetized_list = line.rstrip("\n")
		print(alphabetized_list)
