num =input("enter the num")
reversenumber=0
while num !=0:
    digit=num%10
    reversenumber=reversenumber*10+digit
    num//=10
print(reversenumber)