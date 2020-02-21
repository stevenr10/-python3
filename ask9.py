b=int(input("Δώσε έναν αριθμό:"))
b=b*3+1
e=str(b)
x=len(e)
y=x
p=1
while y>1:
    if p>1 and x>1:
        b=b*3+1
        e=str(b)
        x=len(e)
    a=b
    b=0
    for i in range (x):
        b=b+int(e[i])
        w=str(b)
        y=len(w)
    p=p+1
print (b)
