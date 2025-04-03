students=[
    ("Alice",[85,90,78,92]),
    ("Bob",[60,65,70,75]),
    ("Charlie",[40,45,50,55]),
    ("David",[95,100,98,92])

]
dstudent=dict(students)
print(dstudent)

averages = {key: sum(values) / len(values) for key, values in dstudent.items()}
#print(averages)

print("the avg grades for each student :",averages )

print("The student with highest garde:" ,max(averages))

temp=50

pass_students=sum(1 for marks in averages.values() if marks >= temp)


print("the number of students who passed all subjects",pass_students)
