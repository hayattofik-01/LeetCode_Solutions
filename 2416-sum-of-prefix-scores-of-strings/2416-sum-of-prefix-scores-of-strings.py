class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        
        def insert_in_trie(word):
            cur = trie
            
            for char in word :
                
                if char not  in cur:
                    cur[char] = {}
                    cur[char]['pass'] = 1
                else:
                    cur[char]['pass'] +=1
                    
                cur = cur[char]
        def count_score(word):
            cur = trie
            score = 0
            for char in word:
                score += cur[char]['pass']
                cur = cur[char]
            return score
        
        scores = []
        for word in words:
            insert_in_trie(word)
       
        for word in words:
            scores.append(count_score(word))
        return scores
                
                    
            
            
        