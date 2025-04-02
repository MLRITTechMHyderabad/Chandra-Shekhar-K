'''print("hi");
a=0
if a>0:
    print("+VE")
elif a==0:
    print("zero")
else:
    print("-VE")
'''

li=[1,2,3,4,5,6,7,8]
for i in li:
    print(i)
for i in range(len(li)):
    print("     ",li[i]," ")


print("*************")

li=[[1,2,3],[4,5,6],[6,7,3]]
for i in li:
    print(i)
    for j in i:
        print(j)