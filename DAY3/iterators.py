'''li=[1,2,3,4,5,6]
it=iter(li)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
class MyIter:
    i=0
    def __init__(self,li):
        self.limit=li
        self.start=li[i]
    
    def __iter__(self):
        return self
    def __next__(self):
        i += 1
        if i==len(self.li):
            raise StopIteration
        return self.li[i]
        
o=MyIter(100)
print(next(o))'''


#map function
'''
li=[1,2,3,4,5,6,7,8,9,0]
def sq(x):
  return x*x
x=list(map(lambda x:x*x,li))
print(x)
'''
#filter function

li=[1,2,3,4,5,6,7,8,9,0]

x=list(filter(lambda x:x%2==0,li))
print(x)


