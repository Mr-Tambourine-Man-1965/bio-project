# Homework #3

# assn03-1

for STR in TR-{808..8008}; do echo "$STR"; done


# assn03-2

alias h = 'history'
alias c = 'clear'


# assn03-3

find -name "*.fasta" | wc -l

> There are 15085 .fasta files present


# assn03-4

find -name "*.tre" | wc -l

> There are 14640 phylogenetic trees present


# assn03-5

find -name "*.sched" | wc -l

> There are 15262 analyses that have run


# assn03-6

expr 15085 - 14640

> There are 445 .fasta files that lack a corresponding phylogenetic tree

> I was unable to fully answer this question. I assume that a loop is involved with a wildcard character. The best I could do was separate the two file type into two folders and hope one of them would be filtered to contain the unique fasta files.

find -name '*.fasta' | sort > fasta-files; find -name '*.tre' | sort > tre-files; diff fasta-files tre-files | grep '^<' | wc -l


# assn03-7

showq

> Looks like 87 jobs were successfully submitted to Trestles, while 287 jobs have failed to be included


# assn03-8

> I was unable to present the commands for each of the .fasta files because I could not determine which ones in particular lacked a phylogenetic tree from Question # 6
