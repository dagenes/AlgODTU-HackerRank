#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    maxim = 0
    count = 0
    for i in range(n):
        if(ar[i] > maxim):
            maxim = ar[i]
            count = 1
        elif(ar[i] == maxim):
            count = count + 1

    return count

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
