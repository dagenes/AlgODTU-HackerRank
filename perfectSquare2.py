import math
from itertools import permutations

mySum =0

array = []
stack = []
inputN = int(input())

def permutationsOperation(myList):
    listLength = len(myList)
    myList = list(permutations(myList))
    result = []
    for i in myList:
        number = 0
        for j in range(listLength):
            number += i[j] * 10**(listLength-j-1)
        result.append(number)
    return result


def mahmut(n):
    if n>=81:
        ####push
        stack.append(array)
        n-=81
        array.append(9)
        mahmut(n)
        ####pop
        stack.pop()
    elif n>=64:
        ####push
        stack.append(array)
        n-=64
        array.append(8)
        mahmut(n)
        ####pop
        stack.pop()
    elif n>=49:
        ####push
        stack.append(array)
        n-=49
        array.append(7)
        mahmut(n)
        ####pop
        stack.pop()
    elif n>=36:
        ####push
        stack.append(array)
        n-=36
        array.append(6)
        mahmut(n)
        ####pop
        stack.pop()
    elif n>=25:
        ####push
        stack.append(array)
        n-=25
        array.append(5)
        mahmut(n)
        ####pop
        stack.pop()
    elif n>=16:
        ####push
        stack.append(array)
        n-=16
        array.append(4)
        mahmut(n)
        ####pop
        stack.pop()
    elif n>=9:
        ####push
        stack.append(array)
        n-=9
        array.append(3)
        mahmut(n)
        ####pop
        stack.pop()
    elif n>=4:
        ####push
        stack.append(array)
        n-=4
        array.append(2)
        mahmut(n)
        ####pop
        stack.pop()
    elif n>=1:
        ####push
        stack.append(array)
        n-=1
        array.append(1)
        mahmut(n)
        ####pop
        stack.pop()
    elif n==0:
        #permutations([1, 2, 3])
        deneme = permutationsOperation(array)
        for sayi in deneme:
            if sayi<=inputN:
                global mySum
                mySum+=sayi
                print ("mySum->",mySum,"sayi->",sayi)
                print ("array->",array, "stack->",stack)

sqr_array = []

for i in range (90):
    i=i+1
    sqr_array.append(i*i)

for k in sqr_array:
    mahmut(k)
print(mySum)
#print (sayilar)
