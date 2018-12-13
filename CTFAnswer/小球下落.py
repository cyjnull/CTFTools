a = [0 for x in range(65536)]
for i in range(0,12345):
    tmp=1
    for x in range(0,15):

        if(a[tmp]==0):
            a[tmp]=~a[tmp]
            tmp=tmp*2
        else:
            a[tmp]=~a[tmp]
            tmp=tmp*2+1

        if(i==12344):
            print(tmp)