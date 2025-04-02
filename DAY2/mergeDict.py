'''d1={"a":1,"b":2,"c":3}
d2={"d":4,"e":5,"f":6}

print(d1)
print(d2)

merge_dict={**d1,**d2}
print(merge_dict)'''
'''
d1={"a":1,"b":2,"c":3}
d2={"b":4,"c":5,"d":6}

print(d1)
print(d2)

merge_dict={**d1,**d2}
print(merge_dict)'''
d1={"a":1,"b":2,"c":3}
d2={"b":4,"c":5,"d":6}

print(d1)
print(d2)

merge_dict=d1.copy()
for key,value in d2.items():
    merge_dict[key]=value
print(merge_dict)