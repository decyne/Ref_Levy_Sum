from RefMap import RefMap
from RefValues import RefValues
import csv
import sys

REF_COLUMN = 1
ASSESSOR_COLUMN = 2
OUTPUT_NAME = "output.csv"

# Accepts a 2d matrix and converts it to a csv file
def exportToCSV(matrix2D):
	# Write to csv file
	with open(OUTPUT_NAME,"w") as total_csv:
		writer = csv.writer(total_csv)
		writer.writerows(matrix2D)

def transposeMatrix(matrix2D):
	return [list(x) for x in zip(*matrix2D)]

# Orders all of the referees into a single list and adds a list of levies for each round
def concatonateLevies(round_list):
	# Sum all the levies and add the sum to the end of the list
	merged_round = sum(round_list)
	round_list.append(merged_round)
	referee_list = list(merged_round.rmap.keys())
	
	# Iterate over the list to get the levy for each round and place it in the correct spot corrosponding
	# to the total referee list
	total_levies = []
	total_levies.append(referee_list)
	for round in round_list:
		round_levies = []
		for referee in referee_list:
			round_levies.append(round.getLevy(referee))

		total_levies.append(round_levies)
	
	# Get list of names
	name = []
	name.append("Referee")
	for round in round_list:
		name.append(round.name)

	# Transpose levy matrix and add names to get a nice format :)
	total_levies = transposeMatrix(total_levies)
	total_levies.insert(0, name)

	return total_levies

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

exportToCSV(concatonateLevies(round_list))
