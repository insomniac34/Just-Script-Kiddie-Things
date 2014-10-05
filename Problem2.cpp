/*
															CS-1645 Homework 4, Problem 2
															    Written by Tyler Raborn

							This program calculates the efficiency and speedup of the algorithm modeled by the following runtimes

															serial: T1 = n^2
															parallel: Tp = (n^2 / p) + log2(p)
*/

#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <fstream>
#include <string.h>

#define NANOSECONDS 10000000
#define OUTPUT_BUFFER_SIZE 32

static int num_processors;
static int data_count;
static float efficiency;
static float speedup;

static int n_values[6] = {10, 20, 40, 80, 160, 320};
static int p_values[8] = {1, 2, 4, 8, 16, 32, 64, 128};

int main(int argc, char **argv)
{
	if (argc != 1 && argc != 3)
	{
		printf("Invalid number (%d) of arguments. Usage: ./program <cpu count> <data count> OR ./program for hard-coded test dump to file.\n", argc);
		return -1;
	}
	else if (argc == 1)
	{
		char OUTPUT_data_count[OUTPUT_BUFFER_SIZE];
		char OUTPUT_num_processors[OUTPUT_BUFFER_SIZE];
		char OUTPUT_speedup[OUTPUT_BUFFER_SIZE];
		char OUTPUT_efficiency[OUTPUT_BUFFER_SIZE];
		
		std::ofstream output_stream("problem2_output.txt");

		for (int n = 0; n < 6; n++)
		{
			data_count = n_values[n];
			for (int p = 0; p < 8; p++)
			{
				num_processors = p_values[p];

				float serial_time = pow(data_count, 2) * NANOSECONDS;
				float parallel_time  = ((pow(data_count, 2) / num_processors) + log2(num_processors)) * NANOSECONDS;

				speedup = serial_time / parallel_time;
				efficiency = speedup / num_processors;

				snprintf(OUTPUT_data_count, OUTPUT_BUFFER_SIZE, "%d", data_count);
				snprintf(OUTPUT_num_processors, OUTPUT_BUFFER_SIZE, "%d", num_processors);
				snprintf(OUTPUT_speedup, OUTPUT_BUFFER_SIZE, "%f", speedup);
				snprintf(OUTPUT_efficiency, OUTPUT_BUFFER_SIZE, "%f", efficiency);

				std::string OUTPUT = ("Data for {n = " + std::string(OUTPUT_data_count) + ", p = " + std::string(OUTPUT_num_processors) + "}: \nSPEEDUP = " + std::string(OUTPUT_speedup) + " \nEFFICIENCY = " + std::string(OUTPUT_efficiency) + "\n");
	
				output_stream << OUTPUT << '\n';

				memset(OUTPUT_data_count, '0', sizeof(OUTPUT_data_count));
				memset(OUTPUT_num_processors, '0', sizeof(OUTPUT_num_processors));
				memset(OUTPUT_speedup, '0', sizeof(OUTPUT_speedup));
				memset(OUTPUT_efficiency, '0', sizeof(OUTPUT_efficiency));
			}
		}
		output_stream.close();
	}
	else //argc == 3
	{
		num_processors = atoi(argv[1]);
		data_count = atoi(argv[2]);

		printf("Calculating speedup and efficiency for %d processors computing %d data elements.\n", num_processors, data_count);

		float serial_time = pow(data_count, 2) * NANOSECONDS;
		float parallel_time  = pow(data_count, 2) / ((num_processors + log2(num_processors))) * NANOSECONDS;

		speedup = serial_time / parallel_time;
		efficiency = speedup / num_processors;

		printf("EFFICIENCY: %f \nSPEEDUP: %f\n", efficiency, speedup);
	}

	return 0;
}