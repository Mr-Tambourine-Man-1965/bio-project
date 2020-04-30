import csv
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("gff")
parser.add_argument("fasta")
args = parser.parse_args()
watermelon = SeqIO.read(args.fasta, "fasta")
with open(args.gff, "r") as gff_file:
	reader = csv.reader(gff_file, delimiter="\t")
	for line in reader:
		if not line:
			continue
		else:
			start_coordinate = int(line[3])
			end_coordinate = int(line[4])
			feature = line[2]
			form = line[8]
			if feature == "CDS":
				sequence = watermelon.seq[start_coordinate-1:end_coordinate]
				length = len(sequence)
				g_count = sequence.count("G")
				c_count = sequence.count("C")
				gc_content = (g_count + c_count) / length
				GC_content_answer = round(gc_content, 2)
				print(form)
				print(GC_content_answer)
