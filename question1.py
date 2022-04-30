
def findCouple(arr, n):
    
    count = 0
    
    #arr.sort()
    i = 0
    j = 1
    while i < (n-1):
        if (arr[i] == arr[j]):
            count += 1
            j=j+1
            #i = i+2
        
        else:
            i += 1
            
    return count
    
if __name__ =="__main__":
    
    arr = [1, 2, 1, 2, 1]
    n = len(arr)
    
    print(findCouple(arr, n))
