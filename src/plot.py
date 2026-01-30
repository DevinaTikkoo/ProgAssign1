import matplotlib.pyplot as plt
n = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

matcher_times = [0.058, 0.018, 0.016, 0.016, 0.015, 0.016, 0.019, 0.033, 0.129, 0.748, 6.632, 53.896]
verifier_times = [0.021, 0.015, 0.016, 0.015, 0.015, 0.017, 0.017, 0.023, 0.061, 0.132, 0.538, 2.361]

plt.figure()
plt.plot(n, matcher_times, marker="o")
plt.xlabel("Number of hospitals/students")
plt.ylabel("Running time (seconds)")
plt.title("Matcher Running time vs Number of hospitals/students")
plt.grid(True)
plt.savefig("plot/matcher_plot.png")
plt.show()

plt.figure()
plt.plot(n, verifier_times, marker="o")
plt.xlabel("Number of hospitals/students")
plt.ylabel("Running time (seconds)")
plt.title("Verifier Running time vs Number of hospitals/students")
plt.grid(True)
plt.savefig("plot/verifier_plot.png")
plt.show()