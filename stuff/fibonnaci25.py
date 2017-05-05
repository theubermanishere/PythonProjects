f1 = 1
f2 = 1
ff=1
i=2
##while(ff/(10**1000)!=0):
for a in range(3325):
    i+=1
    f3=f2
    f2=f1+f2
    f1=f2
    ff=f2

print(ff/(10**1000))
print(ff)
print(i)
