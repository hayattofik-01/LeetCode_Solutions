class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3 :
            return False
        p = 0
        while (p < len(arr) and p + 1 < len(arr) and arr[p] < arr[p + 1]):
            p+=1
        if p == len(arr)-1 or p == 0:
            return False
        while(p < len(arr) and p + 1 < len(arr) ):
            if arr[p] <= arr[p+1]:
                return False
            p+=1
        
        return True
            
        
       