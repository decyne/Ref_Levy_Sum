from RefMap import RefMap
from RefValues import RefValues
import csv
import sys

REF_COLUMN = 1
ASSESSOR_COLUMN = 2

# The name of the csv file for each round is passed in as an argument
file_names = sys.argv[1:]

# Keep information about each individual rounde
round_list = []

# Count the levies owed for each referee for each round 
for file_name in file_names:
	# Store the information for each round in the referee map object
	Round = RefMap(file_name)
	with open(file_name, 'rt') as csv_file:
		roster = csv.reader(csv_file)
		for row in roster:
			referee = row[REF_COLUMN]
			assessor = row[ASSESSOR_COLUMN]
			# Increment levies if referee cell is not empty
			if referee:
				Round.incReferee(referee)
			if assessor:
				Round.incAssessor(assessor)

	round_list.append(Round)

for Round in round_list:
	print("----")
	Round.printLevy()

round_list[0] + round_list[1]
