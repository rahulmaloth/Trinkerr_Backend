def groupAnagrams(List):
    result = {}
    
    for s in List:
        key = ''.join(sorted(s))
        
        anagram = result.get((key),[])
        
        anagram.append(s)
        
        result[key] = anagram
    
    return list(result.values())
    
if __name__ == "__main__":
    List = ["idea", "idae", "bsnl", "nsbl", "grasim", "bata"]
    
    print(groupAnagrams(List))
