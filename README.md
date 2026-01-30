# ProgAssign1

# Devina Tikkoo, 61945909
# Hoang Nam Tran, 19547941

# Project Description
This project executes the Gale-Shapely algorithm for hospital-student matching where the hospital is the one proposing. In addition, there is a verifier to check whether the proposed match is valid and has no unstable pairings. 

# Repository Structure 
├── src/
│   ├── matchingengine.py
│   └── verifier.py
├── tests/
│   ├── example.in
│   ├── example2.in
│   ├── example3.in
│   ├── example4.in
│   ├── example1.out
│   ├── example2.out
│   ├── example3.out
│   └── example4.out
├── README.md

# Initial Assumptions: 
Task B requires the out file produced in match A and as the Gale-Shapely algorithm always produced a stable matching, the only way to have INVALID or UNSTABLE output for the verifier is to manually provide a bad matching (.out) file. 

In file formatting:
For task A and task B, we are assuming the input (.in) file contains first line with integer 'n', next 'n' lines are the hospital preference lists, and the following 'n' lines are student preference lists.

Out file formatting: 
The outfile will contain n lines to be placed in the verifier and will always provide a stable matching. It is assumed the outfile from Task A is used as an input for Task B. 

# Running Repository: 
After cloning the repository, run the following commands in command prompt or gitbash. 

Task A: 
python src/matchingengine.py < tests/example.in > tests/example.out

#output will be written to the out file in the tests folder

Task B: 
python src/verifier.py tests/example.in tests/example.out

#output will be either INVALID or UNSTABLE with a short reason, else VALID STABLE

# Provided Examples 
##Note: Running all example files through Task A would result in out files that are valid stable in Task B. The following outcomes are manually written to handle edge cases for Task B. 

1. example.in, example.out is a valid and stable match for when n = 3

2. example2.in, example2.out is a valid but unstable match for when n = 2. There is a blocking pair that prevents stability. 

3. example3.in, example3.out is an invalid matching where n = 2. Student 2 is matched to hospitals 2 and 3, and hospital 3 has no unique student, meaning it should fail the validity check due to duplicate matching.

4. example4.in, example4.out is an edge case where n =8, but only has 7 student preference lists. As n is unequal, running it through Task A would result in an error statement and fail the validity check for Task B. 

