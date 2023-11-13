from collections import defaultdict , deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        # create adjecency list, pattrn - > words that lay in that pattern
        adj_list = defaultdict(list)
        
        for word in wordList:
            for idx in range(len(word)):
                # * on that index and the rest the same with word
                pattern = word[:idx] + "*" + word[idx + 1:]
                
                adj_list[pattern].append(word)
        
        # search for the shortest path between beiginword and end and return the level
        que = deque()
        que.append(beginWord)
        visited = set()
        level = 1
        while que:
            queLen = len(que)
            # hold the current level and add on levels when increase in level
            for curlevel in range(queLen):
                word = que.popleft()
                visited.add(word)
                # if end reached stop instantly 
                if word == endWord:
                    return level
                #search its neighbours using each pattern from it
                for idx in range(len(word)):
                    pattern = word[:idx] + '*' + word[idx + 1:]
                    
                    for neighbour in adj_list[pattern]:
                        if neighbour not in visited:
                            que.append(neighbour)
            level += 1
        return 0
                            
                    
                
                
            
        