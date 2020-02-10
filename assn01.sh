# BIOL 5153 Homework 1


## assn01-1
find $HOME -name "nad*"


## assn01-2
**htop**

> 12 processes found, 2.27Gbs of RAM used out of 47Gbs or about 5%

**top**

top - 15:38:36 up 21 days,  9:27,  1 user,  load average: 0.18, 0.17, 0.24
Tasks: 369 total,   1 running, 284 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.4 us,  0.1 sy,  0.0 ni, 99.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 49245588 total,  1567476 free,  2177520 used, 45500592 buff/cache
KiB Swap: 31999996 total, 31994864 free,     5132 used. 46278480 avail Mem

## assn01-3
**grep misc-feature watermelon.gff | sort -k7gr > IR_regions.gff**

## assn01-4
**grep misc_feature watermelon.gff | less -SN**

> 37 fragments found

**grep -v misc_feature watermelon.gff | less -SN**

> 107 fragments found

> There are more fragments from outside the IR region than from inside according to the numbers

## assn01-5
**cat *.fasta | grep -v GAATTC | grep -1 GGATCC**

> There are 5 genes found to have a BamHI site, but lack an EcoRI

## assn01-6
**cat shaver_et_al.csv | head -n 1000 | tail -n 500 | less -SN**

## assn01-7
**sort -k2,2r -k3,3 fruit.txt | column -t**
