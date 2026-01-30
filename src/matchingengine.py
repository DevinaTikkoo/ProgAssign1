#Task A: Matching Engine: Implement the hospital-proposing deferred acceptance algorithm
# Initially, all hospitals are unmatched and have not proposed to anyone.
# While there exists an unmatched hospital that still has students left to propose to:
# The hospital proposes to the next student on its preference list that it has not yet proposed to.
# The student tentatively accepts the best hospital (according to the student's preferences) among its current tentative match (if any) and the new proposer, rejecting the other.

#pseudocode
#Initialize each person and hospital to be free.
#while (some hospital is free and hasn’t been matched/assigned to every applicant) {
#Choose such a hospital h 
#a = 1st applicant on h's list to whom h has not been matched
#if (a is free)
#assign h and a
#else if (a prefers h to her/his current assignment h')
#assign a and h, and h’ has a slot free
#else
#a rejects h
#}

input_lines = []
#clean edge case input
#read input
#remove whitespace and empty lines
for line in open(0):
    clean_line = line.strip()
    if clean_line != "":
        input_lines.append(clean_line)
#First line: integer n.
#Next n lines: hospital preference lists.
#Next n lines: student preference lists.
n = int(input_lines[0])
hospital_preferences = []
student_preferences = []
#next n lines: hospital preference lists
for i in range(1, n + 1):
    pref_list = []
    for val in input_lines[i].split():
        #convert to 0-indexed
        pref_list.append(int(val) - 1)
    hospital_preferences.append(pref_list)
for i in range(n + 1, 2 * n + 1):
    pref_list = []
    for val in input_lines[i].split():
        #convert to 0-indexed
        pref_list.append(int(val) - 1)
    student_preferences.append(pref_list)
#smaller number higher pref
student_rank_table = []
for student in range(n):
    rank_row = [0] * n
    for pos in range(n):
        hospital = student_preferences[student][pos]
        rank_row[hospital] = pos
    student_rank_table.append(rank_row)

#init
hospital_student = [-1] * n
student_hospital = [-1] * n
next_proposal = [0] * n

while True:
    free_hospital = -1
    for hospital in range(n):
        if hospital_student[hospital] == -1 and next_proposal[hospital] < n:
            #free and still have students left
            free_hospital = hospital
            break
    if free_hospital == -1:
        break
    proposed_student = hospital_preferences[free_hospital][next_proposal[free_hospital]]
    next_proposal[free_hospital] += 1
    #student free, accept proposal
    if student_hospital[proposed_student] == -1:
        student_hospital[proposed_student] = free_hospital
        hospital_student[free_hospital] = proposed_student
    else:
        current_hospital = student_hospital[proposed_student]
        #prefer other -> trade up
        if student_rank_table[proposed_student][free_hospital] < student_rank_table[proposed_student][current_hospital]:
            student_hospital[proposed_student] = free_hospital
            hospital_student[free_hospital] = proposed_student
            hospital_student[current_hospital] = -1 #free up
#output mathcing
#i j 
#hospital i is matched to student j.
for hospital in range(n):
    print(hospital + 1, hospital_student[hospital] + 1)

#how to test with example input
#python matchingengine.py < example.in