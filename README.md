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
python src/verifier.py tests/example.in tests/match.out

#output will be either INVALID or UNSTABLE with a short reason, else VALID STABLE

# Provided Examples 
