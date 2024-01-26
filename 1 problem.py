list1=[7,8,1,3,4,6,7,5]
list2=[]

for i in range(len(list1)):
    if not i % 2:
        list2.append(list1[i]**2)
    else:
        list2.append(list1[i]**3)
print(list2)
print(list1)