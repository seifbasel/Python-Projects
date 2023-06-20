arr=[1,2,3,4,5,6,7,8]

def repeat(arr):
    for i in range(len(arr)):
        for n in range(len(arr)):
            if arr[i]==arr[n] and i != n:
               return False
    return True

print(repeat(arr))
