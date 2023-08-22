ptALimit , ptBLimit = map(int,input().split())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
 
 
limit = min(ptALimit,ptBLimit)
pt1 = 0
pt2 = 0
ans = []
while pt1 < limit and pt2 < limit:
    if list1[pt1] < list2[pt2]:
        ans.append(list1[pt1])
        pt1 +=1
    else:
        ans.append(list2[pt2])
        pt2 +=1
        
    
    
    
    
ans.extend(list1[pt1:ptALimit])
ans.extend(list2[pt2:ptBLimit])
print(*ans)
   
        
    
