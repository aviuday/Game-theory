#!/bin/bash

# Set the number of times to run the Python program
num_runs=10

# Create a new CSV file to store the outputs
output_file=output.csv

# Write the headers to the CSV file
# echo "DA, Random-DA, Better-DA, Worse-DA, Max-Matching, Random-MM, Better-MM, Worse-MM, Top-Trading-Cycle, Random-TTC, Better-TTC, Worse-TTC" > $output_file
echo "Mentor-Utility-DA, Mentor-Utility-Random" > $output_file
# Loop through and run the Python program multiple times
for i in $(seq 1 $num_runs)
do
    # Run the Python program and capture the outputs
    output_da=$(python3 Defered_Acceptance/compare_da.py $i)

    # Parse the two outputs from the Python program
    output1=$(echo $output_da | cut -d' ' -f1)
    output2=$(echo $output_da | cut -d' ' -f2)
    # output11=$(echo $output_da | cut -d' ' -f3)
    # output22=$(echo $output_da | cut -d' ' -f4)

    # output_mm=$(python3 Max_Matching/compare_max_matching.py $i)

    # Parse the two outputs from the Python program
    # output3=$(echo $output_mm | cut -d' ' -f1)
    # output4=$(echo $output_mm | cut -d' ' -f2)
    # output33=$(echo $output_mm | cut -d' ' -f3)
    # output44=$(echo $output_mm | cut -d' ' -f4)

    # output_ttc=$(python3 Top_Trading_Cycle/compare_ttc.py $i)

    # # Parse the two outputs from the Python program
    # output5=$(echo $output_ttc | cut -d' ' -f1)
    # output6=$(echo $output_ttc | cut -d' ' -f2)
    # output55=$(echo $output_ttc | cut -d' ' -f3)
    # output66=$(echo $output_ttc | cut -d' ' -f4)

    # Write the outputs to the CSV file
    # echo "$output1, $output2, $output11, $output22,  $output3, $output4, $output33, $output44, $output5, $output6, $output55, $output66" >> $output_file
    echo "$output1, $output2" >> $output_file
done



# Print a message indicating the script has finished running
echo "Script completed."
