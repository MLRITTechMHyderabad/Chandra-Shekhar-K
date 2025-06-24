'''Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
'''
class Person:
    def getGender(self):
        pass

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"


m = Male()
f = Female()

print(m.getGender())  
print(f.getGender()) 
