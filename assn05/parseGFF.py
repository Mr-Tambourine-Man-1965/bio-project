# Gene List

# First convert "watermelon.gff" into a .csv file
# Type into terminal "gedit parseGFF.py" to create file

file = open("watermelon.gff.csv")
file2 = open("list.txt", "w")
for line in file:
	columns = line.rstrip("\n").split(",")
	gene = columns[8]
	if gene == gene and not gene.startswith("Gene similar"):
		gene2 = gene[5:9]
		file2.write(gene2 + "\n")
	else:
		pass
file2.close()


# Alphabetized Gene List Print

file2 = open("list.txt")
sorted_list = sorted(file2)
for line in sorted_list:
	alphabetized_list = line.rstrip("\n")
	print(alphabetized_list)
