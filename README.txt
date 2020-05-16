Project 2, Team 2:
David Elias	die9
Angela Phillips amp395

===========
input file:
===========
test3a_bin $ python team2_project2.py -i test1_bin.txt -o team2_out_sim

===========
output files:
===========
team2_outdis, 
team2_out_sim, 
team2_out_pipeline.txt

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
5. Enter into the terminal : team2_project2.py -i "C:/(PathToFileLocation)/Project2/test3a_bin.txt" -o "team2_out"
5a. Note that (PathToFileLocation) needs to be the path to where you've saved the project.
6. Hit Enter
7. Output files are saved and updated in the project folder.
8. IMPORTANT: Note that the "team2_out_sim" text file must be cleared manually before each run, otherwise previous runs will persist throughout the file.
