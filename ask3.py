i=0
r=input("Δωσε υλικο:")
t=float(input("Δωσε τιμη:"))
print("Θελετε να αγορασεται και αλλα προϊόντα?")
answer=input("Δωσε απαντηση:")
p=t+t*24/100
pp=t*24/100
while answer=="NAI" or answer=="ναι":
    i=i+1
    r=input("Δωσε υλικο:")
    t=float(input("Δωσε τιμη:"))
    p=p+t+t*24/100
    pp=pp+t*24/100
    print("Θελετε να αγορασεται και αλλα προϊόντα?")
    answer=input("Δωσε απαντηση:")
print (r,t,p,pp)
