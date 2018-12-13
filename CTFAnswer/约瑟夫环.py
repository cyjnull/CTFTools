multiple = 1
a=True
b=True
list = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
while b:
    for i in range(1,13):
        for j in range(24, 11,-1):
            if j == 12:
                b=False
                print(multiple*12+i)
            if list[(multiple*12+i)%j] == 1:
                break
    multiple+=2