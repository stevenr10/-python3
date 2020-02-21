a=input()
s=len(a)
b=""
for i in range (s):
    b=b+str(ord(a[i]))
print (b)
p=2
i=2
w=int(b)
if w==0:
    print("o αριθμος δεν ειναι πρωτος")
else:
    while p==2 and i<=(w-1):
        q=w%i
        print(q)
        if q==0:
            p=p+1
        i=i+1
    if p>2:
        print ("Ο άριθμος δεν είναι πρώτος")
    else:
        print ("Ο άριθμος είναι πρώτος")
