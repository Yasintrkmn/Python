# The problem: https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    app,org=0,0
    for i in apples:
        app += ((i+a) >=s) & ((i+a) <=t)

    for j in oranges:
        org += ((j+b) >=s) & ((j+b) <=t)
    print("{}\n{}".format(app,org))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
