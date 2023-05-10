class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        adj_list = defaultdict(list)
        inDegree = defaultdict(int)
        cooked = []
        for rec,ing in zip(recipes,ingredients):
            inDegree[rec] = len(ing)
            
            for i in ing:
                adj_list[i].append(rec)
        
        que = deque(supplies)
        recipes = set(recipes)
        
        while que:
            
            curSup = que.popleft()
            
            for child in adj_list[curSup]:
                
                inDegree[child] -=1
                
                if  inDegree[child] == 0:
                    que.append(child)
                    cooked.append(child)
        return cooked
                
                
                
                
            
            
        