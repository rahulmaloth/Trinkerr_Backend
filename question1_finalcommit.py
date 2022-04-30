
    
def findCouple(arr):
    
    count = 0
    c_dict = {}
    for i in arr:
        if i in c_dict.keys():
            c_dict[i] = c_dict[i]+1
            
        else:
            c_dict[i] = 1
        
    t = 0
    for i in c_dict.keys():
        k = c_dict[i]
        if k> 1:
            
            ways = k*(k-1)/2
            t = t+ways
            
    return int(t)
    
if __name__ =="__main__":
    
    arr = [1, 2, 1, 2, 1]
    
    print(findCouple(arr))    
