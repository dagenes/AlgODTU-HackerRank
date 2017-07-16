n = int(input())
for i in range (n):
  temp = int(input())
  temp = (2**temp-1) % (10**9)
  print(temp)
