siz = int(input())
graph = []

for i in range(siz):
    lis = list(map(int,input().split()))
    graph.append(lis)

for i in range(len(graph)):
    
    val =[]
    for j in range(len(graph[0])):
        if graph[i][j] == 1:
            val.append(j+1)
  
    print(len(val),*val)
        
           
   
