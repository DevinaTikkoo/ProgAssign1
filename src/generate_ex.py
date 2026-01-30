#create example in files from 1 to 512
sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

for n in sizes:
    file_name = "tests/plot_tests/example_" + str(n) + ".in"
    output_file = open(file_name, "w")
    output_file.write(str(n) + "\n")
    #write hoxpital prefs increasing order
    for hospital in range(n):
        for student_id in range(1, n+1):
            output_file.write(str(student_id) + " ")
            if student_id < n:
                output_file.write(" ")
        output_file.write("\n")
    #student prefs decreasing order
    for student in range(n):
        for hospital_id in range(n, 0, -1):
            output_file.write(str(hospital_id) + " ")
            if hospital_id > 1:
                output_file.write(" ")
        output_file.write("\n")
    output_file.close()
    print(file_name + " generated")