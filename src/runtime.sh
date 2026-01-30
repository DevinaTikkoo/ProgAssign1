#!/bin/bash
n=(1 2 4 8 16 32 64 128 256 512 1024 2048)
for i in "${n[@]}"
do
   echo "Measuring time for n=$i"
   input_file="tests/plot_tests/example_$i.in"
   output_file="tests/plot_tests/example_$i.out"
   #matcher
   echo "matcher:"
   time python src/matcher.py < "$input_file" > "$output_file"
   #verifier
   echo "verifier:"
   time python src/verifier.py "$input_file" "$output_file"
done
#chmod +x src/runtime.sh
#./src/runtime.sh