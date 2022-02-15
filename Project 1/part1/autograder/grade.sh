#!/bin/bash

# Check if we have enough arguments

# Delete temporary files

# Compile the reference program

# Generate reference output files

# Now mark submissions

#
# Note: See Lab02Qn.pdf for format of output file. Marks will be deducted for missing elements.
#

# Iterate over every submission directory
    # Compile C code
    # Print compile error message to output file
    # Generate output from C code using *.in files in ref
    # Compare with reference output files  and award 1 mark if they are identical
# print score for student
# print total files marked.
if [[ $# -eq 0 ]]; then
    echo "Usage: ./grade.sh <filename>"
else
	cd ref
    gcc *.c -o $1
    find . -name "*out" | xargs rm

	total=0
    for filename in *.in; do
		./$1 < $filename > "$filename.out"
		((total++))
    done

	cd ..
	
    echo -e "Test date and time: $(date +%A), $(date +%d) $(date +%B) $(date +%Y), $(date +%T) \n" > result.out

	cd subs
	processed=0

    for student in *; do
	score=0
	error=0
	((processed++))

	cd $student
	gcc *.c -w -o $student 2> gcc_output.txt
	error=$?
	cd ..
	if [[ $error -eq 0 ]]; then
		#Compare files and echo the score
		cd ../ref
		for filename in *.in; do
			../subs/$student/$student < $filename > "$filename$student.out"
			diff "$filename.out" "$filename$student.out" &>/dev/null
			if [[ $? -eq 0 ]]; then
				((score++))
			fi
    	done
		if [[ $error -eq 0 ]]; then
			echo "Directory $student score $score / $total" >> ../result.out
		fi
	else
		echo "Directory $student has a compile error" >> ../result.out
		echo "Directory $student score 0 / $total" >> ../result.out
	fi
	cd ../subs
	done

	echo -e "\nProcessed $processed files" >> ../result.out
fi   
