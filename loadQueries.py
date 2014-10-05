#written by Tyler Raborn 
#converts text files into insert statements for oracle sql...

import os
import sys

def main():

	#outputFileName = sys.argv[1] if len(sys.argv[1]) else 'queries.sql'
	outputFileName = 'queries.sql'

	table_names = ["CUSTOMERS", "CALLS", "STATEMENT", "PAYMENTS", "DIRECTORY"]
	customers_cols = ["ssn", "fname", "lname", "cell_pn", "dob", "home_pn", "street", "city", "zip", "state", "free_min"]
	calls_cols = ["from_pn", "to_pn", "call_timestamp", "duration"]
	statement_cols = ["cell_pn", "start_date", "end_date", "total_minutes", "previous_balance", "amount_due"]
	payment_cols = ["cell_pn", "paid_on", "amount_paid"]
	directory_cols = ["pn", "fname", "lname", "street", "city", "zip", "state"]
	column_values = [customers_cols, calls_cols, statement_cols, payment_cols, directory_cols]

	numericDataTypes = ['amount_paid', 'total_minutes', 'duration', 'previous_balance', 'amount_due']
	temporalDataTypes = ['dob', 'start_date', 'end_date', 'paid_on']

	os.system("rm " + outputFileName)

	with open(outputFileName, 'a') as OUTPUT_FILE:
		with open("sample-data.txt") as INPUT_FILE:
			OUTPUT_FILE.write("set transaction read write name ’test’;\n")
			OUTPUT_FILE.write("set constraints all deferred;\n\n")

			tableIndex = 0
			for line in INPUT_FILE:
				if (not line.isspace()):
					curData = line.split()
					print("LINE: "+str(curData))

					#loop to add special formatting to certain cols
					colIdx = 0
					for column in column_values[tableIndex]:
						if column_values[tableIndex][colIdx] == "street":
							print("converting " + curData[colIdx] + " into " + curData[colIdx] + ' ' + curData[colIdx+1] + ' ' + curData[colIdx+2])
							curData[colIdx] = curData[colIdx] + ' ' + curData[colIdx+1] + ' ' + curData[colIdx+2]
							curData.remove(curData[colIdx+2])
							curData.remove(curData[colIdx+1])							
							break
						colIdx+=1

					#iterate over tokens, if the datatype is NOT numeric, add quotes
					idx = 0
					for token in curData:
						print("token # " + str(idx) + " is " + token)
						if column_values[tableIndex][idx] not in numericDataTypes and column_values[tableIndex][idx] not in temporalDataTypes:
							curData[idx] = "\'"+curData[idx]+"\'"

						if column_values[tableIndex][idx] in temporalDataTypes:
							curData[idx] = 'TO_DATE(\'' + curData[idx] + '\')'
						idx+=1

					curQuery = ("INSERT INTO " + table_names[tableIndex] + " (" + str.join(' ', [(x + ", ") for x in column_values[tableIndex]]) + ") VALUES (" + str.join(' ', [(x + ", ") for x in curData]) + ")").replace(", )", ")")
					curQuery+=';'

					print("Adding query: " + curQuery)
					OUTPUT_FILE.write(curQuery+"\n")

				if (line.isspace()):
					OUTPUT_FILE.write("\n")
					tableIndex+=1
					print("\n SWITCHING CURRENT TABLE TO " + table_names[tableIndex] + "\n")

			OUTPUT_FILE.write("\ncommit;");
		INPUT_FILE.close()
	OUTPUT_FILE.close()

if __name__ == "__main__":
	main()
