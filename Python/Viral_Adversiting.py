#The problem: https://www.hackerrank.com/challenges/strange-advertising/problem

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    liste=[2]
    
    for i in range(n-1):
        x=int(3*liste[i]/2)
        liste.append(x)
        
    return sum(liste)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
