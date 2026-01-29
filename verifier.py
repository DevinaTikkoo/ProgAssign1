# Task B: Verifier
# Write a separate program (or a separate mode in the same program) that:
# (a)  Checks validity: each hospital and each student is matched to exactly one partner, 
# with no duplicates. And (b) checks stability: confirms there is no blocking pair.

import sys

#cleaning instance input and accounting for edge cases

#read input
#argv[1] is instance file, argv[2] is matching output file
instanceLines = []
for line in open(sys.argv[1]):
    clean_line = line.strip()
    if clean_line != "":
        instanceLines.append(clean_line)
matchingLines = []
for line in open(sys.argv[2]):
    clean_line = line.strip()
    if clean_line != "":
        matchingLines.append(clean_line)
#edge case: empty files 
if len(instanceLines) == 0:
    print("INVALID: empty file(s)")
    sys.exit(0)
    
#first line: n hospitals, n students
n = int(instanceLines[0])

#read through preference lists 
hospitalPreferences = []
studentPreferences = []

#Add hospital preferences
for i in range(1, n + 1):
    prefs = [] 
    for val in instanceLines[i].split():
        #convert to 0-indexed
        prefs.append(int(val) - 1)
    hospitalPreferences.append(prefs)

#Add student preferences
for i in range(n + 1, 2 * n + 1):
    prefs = []
    for val in instanceLines[i].split():
        #convert to 0-indexed
        prefs.append(int(val) - 1)
    studentPreferences.append(prefs)

#Utilizing arrays for matching 
hospitalStudent = [-1] * n
studentHospital = [-1] * n

if len(matchingLines) != n:
    print("INVALID: must have n lines")
    sys.exit(0)

#Read through matching pairs
for line in matchingLines:
    parties = line.split()
    hospital = int(parties[0]) - 1
    student = int(parties[1]) - 1

    #Check range
    if hospital < 0 or hospital >= n or student < 0 or student >= n:
        print("INVALID: out of range")
        sys.exit(0)

    #Check duplicates
    if hospitalStudent[hospital] != -1 or studentHospital[student] != -1:
        print("INVALID: duplicates found")
        sys.exit(0)

    #Unique pair, so assign match 
    hospitalStudent[hospital] = student
    studentHospital[student] = hospital

#Check everyone matched 
for i in range(n):
    if hospitalStudent[i] == -1 or studentHospital[i] == -1:
        print("INVALID: unmatched parties")
        sys.exit(0)

#Rank preferences for students and hospitals
hospitalRank = []
studentRank = []

#preference rank for hospitals is [hos][student]
for hos in range(n):
    rankRow = [0] * n
    for p in range(n):
        student = hospitalPreferences[hos][p]
        rankRow[student] = p
    hospitalRank.append(rankRow)

#preference rank for students is [stu][hospital]
for stu in range(n):
    rankRow = [0] * n
    for p in range(n):
        hospital = studentPreferences[stu][p]
        rankRow[hospital] = p
    studentRank.append(rankRow)

#Check stability 
for hos in range(n):
    current = hospitalStudent[hos]
    #Check students preferred over current match 
    for p in range(hospitalRank[hos][current]):
        preferredStudent = hospitalPreferences[hos][p]
        preferredStudentMatch = studentHospital[preferredStudent]
        #Check if preferred student prefers this hospital over their match
        #if so, blocking pair found and unstable
        if studentRank[preferredStudent][hos] < studentRank[preferredStudent][preferredStudentMatch]:
            print("UNSTABLE: blocking pair found")
            sys.exit(0)

#Perfect matching with no unstable pairs means input is stable
print("VALID STABLE")