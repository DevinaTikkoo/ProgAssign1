# ProgAssign1
 1. Devina Tikkoo, 61945909
 2. Hoang Nam Tran, 19547941

## Project Description
This project executes the Gale-Shapely algorithm for hospital-student matching where the hospital is the one proposing. In addition, there is a verifier to check whether the proposed match is valid and has no unstable pairings. 

## Repository Structure

```text
├── plot_images/
│   ├── matcher_runtime.png
│   └── verifier_runtime.png
├── src/
│   ├── matcher.py
│   └── verifier.py
├── tests/
│   ├── plot_images/
│   ├── example.in
│   ├── example2.in
│   ├── example3.in
│   ├── example4.in
│   ├── example1.out
│   ├── example2.out
│   ├── example3.out
│   └── example4.out
└── README.md
```

## Initial Assumptions
1. Task B requires the out file produced in match A and as the Gale-Shapely algorithm always produced a stable matching, the only way to have INVALID or UNSTABLE output for the verifier is to manually provide a bad matching (.out) file. 

2. In file formatting: For task A and task B, we are assuming the input (.in) file contains first line with integer 'n', next 'n' lines are the hospital preference lists, and the following 'n' lines are student preference lists.

3. Out file formatting: The outfile will contain n lines to be placed in the verifier and will always provide a stable matching. It is assumed the outfile from Task A is used as an input for Task B. 

## Running Repository
After cloning the repository, run the following commands in command prompt or gitbash. 

Task A: 
```text
python src/matcher.py < tests/test1.in > tests/test1.out

#output will be written to the out file in the tests folder
```

Task B: 
```text
python src/verifier.py tests/test1.in tests/test1.out

#output will be either INVALID or UNSTABLE with a short reason, else VALID STABLE
```

Task C: 
The above task is portrayed at the bottom of this read me, but step-wise the examples can be generated via running generate_ex.py for n = 1, 2, 4, ..., 2048. After, use runtime.sh to measure the runtime with the following commands:

```text
chmod +x src/runtime.sh

./src/runtime.sh
```

Then, run plot.py and check plot_images for the matcher_plot.png that measures matcher run time compared to n and verifier_plot, which does the same but with the verifier. 

## Provided Examples 
#### Note: Running all example files through Task A would result in out files that are valid stable in Task B. Additionally, edge cases such as empty input files or unequal n will show an error written in the outfile when ran through task A. For task B, the following outcomes have been manually written to demonstrate edge cases.

1. test1.in, test1.out is a valid and stable match for when n = 3

2. test2.in, test2.out is a valid but unstable match for when n = 2. There is a blocking pair that prevents stability. 

3. test3.in, test3.out is an invalid matching where n = 2. Student 2 is matched to hospitals 2 and 3, and hospital 3 has no unique student, meaning it should fail the validity check due to duplicate matching.

4. test4.in, test4.out is an edge case where n =8, but only has 7 student preference lists. As n is unequal, running it through Task A would result in an error statement appearing in the out \file and fail the validity check for Task B. 

## Task C: Scalability 
We measured the running time of the matching engine as well the verifier on separate graphs against increasing values of n. Specifically, we generated data from n = 1, 2, 4, 8, ...2048 using generate_ex,py, measured run time with runtime.sh, and used matplotlib to generate the graphs in plot.py. The graphs can be found below.

![Matcher Running Time](plot_images/matcher_plot.png)

![Verifier Running Time](plot_images/verifier_plot.png)

It is noted that the matcher's runtime increases rapidly as n grows by a factor of 2. The curve mimics quadratic time, which aligns with the theoretical worst-case for Gale-Shapely algorithm being O(n^2) as the n hospitals could propose to n students each. 

The verifier's runtime also increases quadratically, but at a faster rate than the matcher. This is because the verifier checks validity and stability, meaning it requires more nested scans over preference lists. However, it takes in smaller inputs than the matcher, leading to quicker run times. In worst case, the verifier goes through n hospitals with n students each, leading to O(n^2) time. 

