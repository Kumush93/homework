def intToRoman(num:int):
    roman=[" I","IV","V", "IX","X","XL","L","XC","C","CD","D","CM","M"][::-1]
    number=(1000,900,500,400,100,90,50,40,10,9,5,4,1)
    
    s=''
    for i in range (len(number)):
        count=num//number[i]
        s+=roman[i]*count
        num-=number[i]*count
    return s

print(intToRoman(59))
print(intToRoman(100))