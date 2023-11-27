class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = defaultdict(int)
        
        for birth, death in logs:
            years[birth] += 1
            years[death] -= 1
        check = []
        
        for key in years:
            check.append([key,years[key]])
        check.sort()
        max_pop = [check[0][0], check[0][1]]
        for i in range(1,len(check)):
            check[i][1] += check[i - 1][1]
            if check[i][1] > max_pop[1]:
                max_pop = [check[i][0],check[i][1]]
        return max_pop[0]
        
            
            
            
        