# Homework #1

'assn01-1'

find $HOME -name "nad*"


'assn01-2'

htop

> There are 12 processes on this computer and about 5% is currently being used

top

> top - 08:52:15 up  1:39,  1 user,  load average: 0.24, 0.16, 0.19
Tasks: 357 total,   2 running, 274 sleeping,   0 stopped,   0 zombie
%Cpu(s):  1.2 us,  0.3 sy,  0.0 ni, 98.1 id,  0.4 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 49245588 total, 45375744 free,  2212392 used,  1657452 buff/cache
KiB Swap: 31999996 total, 31999996 free,        0 used. 46190172 avail Mem


'assn01-3'

grep misc_feature watermelon.gff | sort -k7gr > IR_regions.gff


'assn01-4'

grep misc_feature watermelon.gff | less -SN

> There are 37 fragments from inside the IR

grep -v misc_feature watermelon.gff | less -SN

> There are 107 fragments from outside the IR

> There are more fragmetns from outside the IR than inside the IR, so it isn't the case


'assn01-5'

cat *.fasta | grep -v GAATTC | grep -1 GGATCC

> There are a handful of watermelon genes that have a BamHI site, but lack amn EcoRI site


'assn01-6'

cat shaver_et_al.csv | head -n 1000 | tail -n 500 | less -SN


'assn01-7'

sort -k2,2r -k3,3 fruit.txt | column -t
