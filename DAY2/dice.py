import random


d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]
li=[]
for i in range(1,7):
    for j in range(1,7):
        li.append((i,j))
print(li)
di={}
for i in range(1,13):
    c=0
    for j in li:
        if i==j[0]+j[1]:
            c+=1

    di[str(i)]=c/len(li)
print("The probs",di)
#ounds =int(input())
p1_d1,p1_d2=random.sample(d1,2)
p2_d1,p2_d2=random.sample(d2,2)
print("Player1:",p1_d1,p1_d2)
print("Player2:" ,p2_d1,p2_d2)
sump1=p1_d1+p1_d2
sump2=p2_d1+p2_d2
if sump1 > sump2:
    print("p1 wins")
elif sump1<sump2:
    print("p2 wins")
else:
    print("DRAW")
   


