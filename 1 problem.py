list1=[7,8,1,3,4,6,7,5]
list2=[]

for i in range(len(list1)):
    if not i % 2:
        list2.append(list1[i]**2)
    else:
        list2.append(list1[i]**3)
print(list2)
print(list1)

x=input("Enter the firts number:")
y=input("Enter the second number:")
z=input("Enter the third number:")
x,y,z=z,x,y
print(f"Firts number {x} , second number {y},third number {z}")
