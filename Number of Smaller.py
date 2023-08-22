ptALimit , ptBLimit = map(int,input().split())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))


limit = min(ptALimit,ptBLimit)
pt1 = 0
pt2 = 0
ans = [ 0 for i in range(ptBLimit)]

for i in range(ptBLimit):
    while pt1  < ptALimit and list2[i] > list1[pt1]:
        ans[i ] +=1
        pt1 +=1
for i in range(1,ptBLimit):
    ans[i] +=ans[i -1 ]
    
    

print(*ans)
   
        
    
    

