#written by Tyler Raborn for CS1645 homework 7 results analysis

#required ordering of input file: 
#<node_count>
#<particle_count>
#<time>

#<node_count>
#<particle_count>
#<time>

#<node_count>
#<particle_count>
#<time>
#...

import sys

def main():

	node_count = 0
	particle_count = 0
	time = 0

	speedup = 0.0
	efficiency = 0.0

	linear_time_A = 14194.51
	linear_time_B = 225449.00
	linear_time_C = 3734942.02

	print("Beginning processing of results...")
	with open("final_results.txt") as INPUT_FILE:

		iter_count = 0
		for line in INPUT_FILE:

			if line == "END":
				break

			elif line.isspace():
				if particle_count == 16384:
					speedup = linear_time_A / time
				elif particle_count == 65536:
					speedup = linear_time_B / time
				elif particle_count == 262144:
					speedup = linear_time_C / time

				print("SPEEDUP with " + str(particle_count) + " particles on " + str(node_count) + " nodes: " + str(speedup))
				efficiency = speedup / node_count
				print("EFFICIENCY with " + str(particle_count) + " particles on " + str(node_count) + " nodes: " + str(efficiency)) + "\n"

			else:
				if iter_count == 0:
					node_count = int(line)
				elif iter_count == 1:
					particle_count = int(line)
				elif iter_count == 2:
					time = float(line)

				iter_count+=1

				if iter_count == 3:
					iter_count = 0				

	INPUT_FILE.close()

if __name__ == "__main__":
	main()

