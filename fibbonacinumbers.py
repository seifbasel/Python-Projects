# def fib(n):
#     a=0
#     b=1
#     for i in range(0,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
    
        
# print(fib(5))

def fip(f):
    if f==0: 
        return 0
    elif f==1:
        return 1
    else:
        return fip(f-1)+fip(f-2)

print(fip(8))