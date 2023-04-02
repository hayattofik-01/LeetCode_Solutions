siz = int(input())
for i in range(siz):
    x=int(input())
    y=x&-x
    while (x==y or (x&y)==0):
    	y+=1
    print(y)
            
  
            
        
