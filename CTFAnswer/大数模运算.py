a=3
b=5
c=823
m=9901

aa=0
bb=0
cc=0

num = 12345
num2 = 0
for i in range(0,1+num):
    aa += a**i
    aa %= m
for i in range(0,1+num):
    bb += b**i
    bb %= m
for i in range(0,1+num):
    cc += c**i
    cc %= m


print(aa*bb*cc%m)