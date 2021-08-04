#!/bin/bash

##	I suppressed error messages on certain comands. To re-enable them, remove the "2>/dev/null" on the code		##
##	If there is any update I should make, or if there is anything I can clarify, please email me at 		##
##	kennethchen2001@gmail.com or kenneth.chen@biola.edu								##	

#downloads new_tardump.tar.gz from ftp.ncbi.nlm.etc...
wget ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.tar.gz

#make "old directory"
mkdir .old 2>/dev/null
mkdir .old/rankedlineage/ 2>/dev/null
mkdir .old/tar/ 2>/dev/null

#move old rankedlineage.dmg file to .old directory
mv rankedlineage.dmp $(date +%Y%m%d)rankedlineage.dmp
mv *rankedlineage.dmp .old/rankedlineage/

#extract new_taxdump.tar.gz
tar -xvf new_taxdump.tar.gz

#run python script to update ranked_lineage_file.csv
python3 csvedit.py

#format: year, month, day
mv new_taxdump.tar.gz $(date +%Y%m%d)new_taxdump.tar.gz

#move modified new_taxdump.tar.gz(+date) to .old_tar
mv *.tar.gz .old/tar/
