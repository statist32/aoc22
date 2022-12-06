#!/bin/sh
day_number=$1;
echo "Created files for day: ${day_number}";

folder="day_${day_number}";
mkdir ${folder};

python_file="${folder}/main.py"
test_data_file="${folder}/input_test.txt"
data_file="${folder}/input.txt"

touch ${test_data_file} ${data_file};
cp template.py ${python_file};