siz = int(input())

for i in range(siz):
    numLen = int(input())
    nums  = list(map(int,input().split()))
    s = cur = 0
    for j in range(numLen):
        
        if nums[j] * cur > 0:
            cur = max(cur,nums[j])
        else:
            s += cur 
            cur = nums[j]
    print(s + cur)
