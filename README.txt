Project 2, Team 2:
David Elias	die9
Angela Phillips amp395

===========
input file:
===========
test3a_bin.txt

===========
output files:
===========
team2_outdis.txt, 
team2_out_sim.txt

================================================================================================================================================================================
Program reads in binary code from an input file (test3a_bin) and translates to ARM: LEGv8 assembly language, then writes the translated ARM assembly to a file(team2_outdis).
Program then executes instruction-by-instruction simulation of the translated ARM: LEGv8 program and writes the state of each cycle to the file(team2_out_sim).
SIMULATOR OUTPUT FILE (team2_out_sim) MUST BE CLEARED BETWEEN RUNS TO PREVENT PREVIOUS RUNS PERSISTING THROUGH THE OUTPUT FILE.
================================================================================================================================================================================
HOW TO RUN:

1. Ensure that python 3 is installed on your system.
2. Unzip and extract the project to your directory of choice
3. Open the terminal(linux/OSX) or Command Prompt(Windows)
4. Change directory to where you've saved the project. 
5. Enter into the terminal : python team2_project2.py -i "C:/(PathToFileLocation)/Project2/test3a_bin.txt" -o "team2_out"
5a. Note that (PathToFileLocation) needs to be the path to where you've saved the project.
6. Hit Enter
7. Output files are saved and updated in the project folder.
8. IMPORTANT: Note that the "team2_out_sim" text file must be cleared manually before each run, otherwise previous runs will persist throughout the file.
=================================================================================================================================================================================
CONTENTS:

test3a_bin.txt:	
	This files contains the raw LEGv8 binary instructions that will be simulated. Note that a special BREAK instruction is included near the end of the file;
11111110110 11110 111111 11111 00111. Binary following after this break will be treated as raw data and stored as such.

team2_outdis.txt:
	This file shows the raw binary instruction alongside it's corresponding assembly language translation.

team2_out_sim.txt:
	This file shows the simulated run of the translated machine code.
Looking at an isolated cycle of the simulation we can see the following. Reading from left to right, top to bottom:

					===============
					cycle:1	96	ADDI	R4, R4, #160

					registers:
					r00:	0	0	0	0	160	0	0	0
					r08:	0	0	0	0	0	0	0	0
					r16:	0	0	0	0	0	0	0	0
					r24:	0	0	0	0	0	0	0	0

					data:
					176:-1	-2	-3


Firstly the cycle counter, which increments with each instruction processed. Currently, since we are looking at the first instruction processed this is 1.

Next we have the program counter. This starts at 96 and is incremented by 4 every instuction.

Following the program counter is the instruction being processed; ADDI R4,R4, #160 in this case.

Below the first line we have a table displaying the registers and their contents. 32 registers are displayed in total with 8 registers listed per row. Registers are
zero based, so the first row of registers (r00) contains registers r0 - r7 and so on.

At the very bottom of each cycle is the data found after the break instruction. The number preceding the data (176 in this case) is where the data is located on the program counter. 
=================================================================================================================================================================================

For more information on each file individually, read the comment block at the top of each file.





