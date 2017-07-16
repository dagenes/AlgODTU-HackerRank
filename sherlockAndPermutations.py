import math
from decimal import Decimal

def floatToString (inputValue, precision = 0):
    rc = str(Decimal(inputValue).normalize())
    if 'E' in rc or len(rc) > 5:
        rc = '{0:.{1}g}'.format(inputValue, precision)
    return rc

n = int(input())
for i in range (n):
    temp = ""
    temp = raw_input()
    liste = temp.split(' ')

    temp = float(liste[0])
    temp2 = float(liste[1])

    sonuc = math.factorial(temp+temp2-1)/ (math.factorial(temp)*math.factorial(temp2-1))
    sonuc = (sonuc) % (10**9+7)
    sonuc = "{:.0f}".format(sonuc)
    print(sonuc)
