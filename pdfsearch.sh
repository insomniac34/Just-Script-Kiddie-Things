#!/bin/bash
#searches through the current directory's pdf files for the passed-in string argument 

red='\e[0;31m' #color
NC='\e[0m' # no color

for f in `ls *.pdf`
do
	echo -e "${red}RESULTS FROM $f:${NC}"
	pdftotext $f temp.txt
	cat temp.txt | grep --color=auto $1
	rm temp.txt
	echo " "
done
