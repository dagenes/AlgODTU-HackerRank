import math

def perfectSquare(number):
    t = int(math.sqrt(number))
    print("t->",t,"number->", number)
    if t*t == number:
        #print("True")
        return True
    else:
        return False

n = int(input())

sum23 =0
sayilar = []
for i in range(n+1):
    sum = 0
    sayi = i
    while i>0:
        temp=i%10
        i=i/10
        sum += (temp**2)
    if perfectSquare(sum):
        sayilar.append(sayi)
        sum23=sum23+sayi
sum23=sum23%(10**9+7)
print(sum23)
#print (sayilar)
