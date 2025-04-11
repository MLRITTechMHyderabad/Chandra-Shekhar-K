li=[1,2,8,9,4,2,1,5,6,7,6,3,3,9,8]
li=sorted(li)
freq={}
for i in li:
    if i in freq:
        freq[i] +=1
    else:
        freq[i]=1
print(freq)