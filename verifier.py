# Task B: Verifier
# Write a separate program (or a separate mode in the same program) that:
# (a)  Checks validity: each hospital and each student is matched to exactly one partner, 
# with no duplicates. And (b) checks stability: confirms there is no blocking pair.

import sys

#helper function to clean files
def clean(path):
    lines = []
    for ln in open(path):
        if ln.strip() != "":
            lines.append(ln.strip())
    return lines


#validate argument count 

instanceFile = sys.argv[1]
matchingFile = sys.argv[2]

cleanInstance = clean(instanceFile)
#Check file has content
#Assuming have n hospitals and n students
n = int(cleanInstance[0])

hospitalPreference = []
for i in range(1, n+1):
    r = [] 
    for j in cleanInstance[i].split():
        r.append(int(j) - 1)
    hospitalPreference.append(r)


