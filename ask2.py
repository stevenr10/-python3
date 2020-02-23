word=input()
length=len(word)
print(word,length)
badletter=0
consonants=0
for i in range (length):
    if word[i]=="f" or word[i]=="c" or word[i]=="k" or word[i]=="r" or word[i]=="F" or word[i]=="C" or word[i]=="K" or word[i]=="R":
        badletter=badletter+1
    if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u" or word[i]=="y" or word[i]=="A" or word[i]=="E" or word[i]=="O" or word[i]=="U" or word[i]=="Y" or word[i]=="I":
        consonants=consonants+1
diafor=length-consonants
diafora=diafor-badletter
if diafora<=badletter:
    print("Η λεξη ειναι κακη")
else:
    print ("Η λεξη ειναι καλη")
