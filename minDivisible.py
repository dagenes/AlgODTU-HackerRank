import time
import math

def ilen(sayi):
    return int(math.log10(sayi))+1

def lastndigit(sayi, n):
    return sayi % 10**n

def test (sayi, w):
    t = 0
    c = 1

    for n in range(1,w+1):
        d = sayi // 10**(w-n) % 10
        #print w, " ", n
        if d == 0 or c - t > w - n:
            return w-(n-1)

        t += d
        c *= d

    if t < c:
        #print "."
        return -1

    print w, " ", sayi
    return -2


import sys

base = int(sys.argv[1])
sayi = base
baselen = ilen(sayi)
done = False

initial = time.time()
i = 0
while not done:
    i += 1
    sayilen = ilen(sayi)
    n = test(sayi, sayilen)

    if n > 0:
        if sayilen > baselen and n > baselen:
            lastNDecimal = 10**(n-1)
            notNeededArea = sayi%10**(n-1)

            difference = lastNDecimal - notNeededArea

            baseMultipler = difference // base if difference > base else 1
            baseMultipler = baseMultipler - 1 if not baseMultipler == 1 else 1

            #print sayilen," ",sayi, " ", n, " ", lastNDecimal, " ", notNeededArea, " ", difference, " ", baseMultipler, " ", base*baseMultipler

            sayi += base*baseMultipler
        else:
            sayi += base
    elif n == -1:
        sayi += base
    elif n == -2:
        done = True

    if(time.time()-initial) > 35:
        print("timeout - ^" + str(i) + ":" + str(sayi))
        break

print((time.time() - initial))
