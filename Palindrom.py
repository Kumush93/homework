def Palindrom(n):
    return str(n)==str(n)[::-1]
n=input("Enter the number:")
print(Palindrom(n))