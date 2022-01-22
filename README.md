# Graduation Problem: Impact Analytics

## Question:

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal

## Test cases:

for 5 days: 14/29

for 10 days: 372/773

## Functions:
 
get_graduation_absent_prob(n): This function calculates the probability of a student missing graduation

get_graduation_attend_prob(n): This function calculates the number of ways to attend classes over N days

get_graduation_probability(days): This function returns the solution of get_graduation_absent_prob(n) / get_graduation_attend_prob(n) as a string

## Execution: 
python <path_to>/graduation_attendance.py

## Testing:
There are sample test cases available in input.txt.
This input.txt file takes the number of days in an academic year as input on a line by line basis and sends as parameter to the function get_graduation_probability()
