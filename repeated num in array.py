arr=[1,2,3,4,5,6,7,8]

def repeated(arr):
    # set removes repeated numbers in list
    if len(set(arr))!=len(arr):
        return True
    return False

print(repeated(arr))
