class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        l = len(s)
        trie = {}
        
        def insert_in_trie(word):
            cur = trie
            for char in word :
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            if None in cur:
                cur[None] +=1
            else:
                cur[None] = 1
        for word in words:
            insert_in_trie(word)       
        que = deque()
        que.append((trie,0))
        count = 0
        while que:
            cur , idx = que.popleft()
            
            for val in cur:
                if val == None:
                    count += cur[None]
                else:
                    for i in range(idx,l):
                        if val == s[i]:
                            que.append((cur[val],i + 1))
                            break
        return count
                        
                    
                    
                    
                    
                    
            
        