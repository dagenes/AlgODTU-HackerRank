import math
from itertools import permutations


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

print len(permutationsOperation([1,2,3,4,5,6]))
