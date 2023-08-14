siz = int(input())
nums = list(map(int,input().split()))
even = 0
odd = 0

for n in nums:
    
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
if even * odd > 0:
    print(*(sorted(nums)))
else:
    print(*nums)
        
