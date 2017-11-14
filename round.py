#!/bin/python3

import sys

def solve(grades):
    temp_list = []
    for i in range(len(grades)):        
        if grades[i] >= 38:
            temp = grades[i] % 10
            if temp == 7:
                #print(grades[i])
                temp_list.append(grades[i])
            elif temp < 7:
                #print(round(grades[i], -1) + 5)
                temp_list.append(round(grades[i], -1) - 5)
            elif temp > 7:
                #print(round(grades[i], -1))
                temp_list.append(round(grades[i], -1))
        else:
            #print("fail")
            temp_list.append(grades[i])
    return(temp_list)
            

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))

