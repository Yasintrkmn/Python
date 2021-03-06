#The problem: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    if year ==1918:
        return "26.09.1918"
      
    if ((year<1918) & (year%4==0)) | ((year%4==0) & (year%100!=0)) | (year%400==0):
        return "12.09.{}".format(year)
      
    else:
        return "13.09.{}".format(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
