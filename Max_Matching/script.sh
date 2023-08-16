#!/bin/bash

# Set the number of times to run the Python program
num_runs=10

# Create a new CSV file to store the outputs
output_file=output.csv

# Write the headers to the CSV file
echo "Max Matching, Random" > $output_file

# Loop through and run the Python program multiple times
for i in $(seq 1 $num_runs)
do
    # Run the Python program and capture the outputs
    output=$(python3 compare_max_matching.py)

    # Parse the two outputs from the Python program
    output1=$(echo $output | cut -d' ' -f1)
    output2=$(echo $output | cut -d' ' -f2)

    # Write the outputs to the CSV file
    echo "$output1, $output2" >> $output_file
    
done

python3 plot.py

# Print a message indicating the script has finished running
echo "Script completed."
