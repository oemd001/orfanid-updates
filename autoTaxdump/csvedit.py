##	If there is anything I should clarify, please don't hesitate to contact me at	##
##	kennethchen2001@gmail.com or kenneth.chen@biola.edu 				##

from csv import writer
from datetime import datetime
import hashlib
import os.path
from os import path
from pathlib import Path

#function that addes a new row after each iteration
def addEntry(fileName, addedText):
	with open(fileName, 'a+', newline='') as write_obj:
		csv_writer = writer(write_obj)
		csv_writer.writerow(addedText)


#creates rank_lineage_versions.csv for the first time
if not(path.exists("rank_lineage_versions.csv")):
	Path("rank_lineage_versions.csv").touch()

#grabs the checksum from "new_taxdump.tar.gz"
currentDatetime = datetime.now()
currentDatetime = str(currentDatetime) + "\t"

with open("rankedlineage.dmp", "rb") as f:
	bytes = f.read()
	sha256hash = hashlib.sha256(bytes).hexdigest()
	sha256hash = str(sha256hash) + "\t"

#version number
with open("rank_lineage_versions.csv") as csvfile:
	count = sum(1 for row in csvfile) + 1
	count = "version " +  str(count) + "\t"

#format: updated date; version of file; SHA256 checksum
newContent = [currentDatetime, count, sha256hash]

#adds the row to the "rank_lineage_versions.csv"
addEntry("rank_lineage_versions.csv", newContent)
