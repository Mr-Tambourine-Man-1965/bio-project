import csv
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("gff")
parser.add_argument("fasta")
args = parser.parse_args()
watermelon = SeqIO.read(args.fasta, "fasta")
with open(args.gff, 'r') as gff_file:
	reader = csv.reader(gff_file, delimiter="\t")
	for line in reader:
		if not line:
			continue
		else:
			start_coordinate = line[3]
			end_coordinate = line[4]
			print(start_coordinate, end_coordinate)
gene_names = []
