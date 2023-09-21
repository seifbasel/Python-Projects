def prime_checker(number):
    is_prime_num=True
    
    for i in (2,number):
       if number%i==0:
        is_prime_num=False
        
    if is_prime_num==True:
        print(f"{number} is a prime num")
    else:
        print(f"{number} is not a prime num")

number1=int(input("enter the num: "))
prime_checker(number1)
