#!/bin/bash
echo "Enter the first number: "
read NUM1
echo "Enter the second number: "
read NUM2
if [[ NUM1 -eq NUM2 ]]; then
echo "$NUM1 = $NUM2"
elif [[ NUM1 -gt NUM2 ]]; then
echo "$NUM1 > $NUM2"
else
echo "$NUM1 < $NUM2"
fi
