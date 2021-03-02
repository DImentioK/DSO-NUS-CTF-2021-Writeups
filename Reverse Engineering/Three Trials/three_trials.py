import math

arg1,arg2,arg3= 0,0,0

for k in range(400,800):
    res=0
    val=k
    while(val>0):
        res+=pow((val%10),3)
        val//=10
    if(res==k):
        arg1=k
        print("arg 1 =",arg1)
        break

##for i in range(1,100000):
##    k=pow(i,2)
##    if(k<10):
##        continue
##    else:
##        res=int(str(k)[::-1][:-1][::-1])+int(str(k)[0])
##        if(res==i):
##            arg2=i
##            print("arg 2 =",arg2)
def check(val):
    numDigits=len(str(pow(val,2)))
    valS=pow(val,2)
    for k in range(1,numDigits):
        div=pow(10,k)
        if(val==(valS%div + valS//div)):
            print("arg 2 =",val,"k=",k)
for i in range(4,100000):
    check(i)
# https://oeis.org/A000396
perfect=[6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 2658455991569831744654692615953842176, ]

for k in perfect:
    if k> pow(10,5) and k < pow(10,8):
        arg3=k
        print("arg 3 =",arg3)
        break
