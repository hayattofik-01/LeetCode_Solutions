class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_length = float('-inf')
        
        # use prefix_size to check if the remaining array can produce possible larger unique string
        prefix_size = [0] * len(arr)
        prefix_size[-1] = len(set(list(arr[-1])))
        
        for i in range(len(arr)-2, -1, -1):
            prefix_size[i] = len(set(list(arr[i]))) + prefix_size[i+1]    
        
        # print(prefix_size)
        def backtrack(arr, string, index=0):
            nonlocal max_length
            # before we go deeper backtrack, 
            # we check if the remaining array can produce possible larger unique string,
            # if current string, presumbly unique, plus the remaining possible unique string has length smaller than current maximum length, 
			# then we don't need to go deeper, just return.
            if index < len(prefix_size) and len(string) + prefix_size[index] < max_length:
                return
            
            if len(string) > max_length and len(string) > 0:
                max_length = len(string)
            
            if index == len(arr):
                return
            
            for i in range(index, len(arr)):
                set1 = set(string)
                set2 = set(list(arr[i]))
                union = set1.union(set2)
                
                # must check if the union set size is equal to the array size sum so to make sure they are all unique
                if len(union) == len(string) + len(arr[i]):
                    for c in set2:
                        string.append(c)
                    backtrack(arr, string, i + 1)
                    for c in range(len(arr[i])):
                        string.pop()
            return
        
        
        backtrack(arr, [], 0)
        return max_length if max_length != float('-inf') else 0