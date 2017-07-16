import time

initial = time.time()

def mustafa (sayi):
    toplam = 0
    carpim = 1
    if "0" in sayi:
        return False

    #print (sayi + "->mustafa")

    for i in range(len(sayi)):
        toplam += int(sayi[i])
        carpim *= int(sayi[i])
        #print ("\t carpim-toplam = " + str(carpim - toplam))
        if (carpim - toplam) > (len(sayi) - (i+1)):
            return False


    if toplam < carpim:
        return False
    return True


alSayi = str(input())
base  = int(alSayi)
hello = mustafa(alSayi)
if hello:
    print (len(alSayi))
else:
    alSayi = str(int(alSayi) + base)
    while not mustafa(alSayi):
        alSayi = str(int(alSayi) + base)
        if((time.time() - initial) > 320000):
            print ( "Time out !")
            break
    print (len(alSayi))

#print((time.time() - initial))
