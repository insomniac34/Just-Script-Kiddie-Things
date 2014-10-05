#	Written by Tyler Raborn
#	Calculates Speedup for Tabulated Program Results


cnt = 0
serial_time = ' '
current_time = ' '
num_threads = ' '
problem_size = ' '
speedup = 0
efficiency = 0

RESULTS_FILE = open('gaussian_final_results.txt', 'a')

with open('gaussian_input_results.txt', 'r') as FILE:
		for line in FILE:

			problem_size = line.split()[0]
			num_threads = line.split()[1]
			current_time = line.split()[2]


			if cnt == 0 or cnt == 5 or cnt == 10:
				serial_time = current_time

			#print ("speedup is " + serial_time + " / " + current_time + '\n')
			speedup = float(serial_time) / float(current_time)
			#print ("efficiency is " + str(speedup) + " / " + current_time + '\n')
			efficiency = speedup / float(num_threads)

			RESULTS_FILE.write('./Gaussian ' + problem_size + ' ' + num_threads + ' ' + serial_time + '\n')
			RESULTS_FILE.write('speedup: ' + str(speedup) + '\n')
			RESULTS_FILE.write('efficiency: ' + str(efficiency) + '\n\n')

			cnt+=1

