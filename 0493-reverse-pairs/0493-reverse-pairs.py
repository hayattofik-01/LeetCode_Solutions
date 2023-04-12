import math
class Solution:
    # TIME n*(logn)*(logn)
    def floor(self, li, key):
        i,j = 0, len(li)-1
        pos = -1
        while i <= j:
            mid = (i+j)//2
            if li[mid] < key:
                pos = mid
                i = mid+1
            else:
                j = mid-1
        return pos
    
    def merge(self, li, l, m, r):
        L, R,n1,n2 = [],[], m-l+1, r-m
        for i in range(n1):
            L.append(li[l+i])
        for i in range(n2):
            R.append(li[m+1+i])
        
		######ANSWER LOGIC#######
        for i in range(n1):
            key = math.ceil(L[i]/2)
            j = self.floor(R, key)
            if j!=-1:
                self.count += j+1
                
        ######MERGE LOGIC########
        i,j,k=0,0,l        
        while i<n1 and j<n2:
            if L[i] <= R[j]:
                li[k] = L[i]
                i+=1
            else:
                li[k] = R[j]
                j+=1
            k+=1
        while i<n1:
            li[k] = L[i]
            i+=1
            k+=1
        while j<n2:
            li[k] = R[j]
            j+=1
            k+=1
    
    def merge_sort(self, li, i, j):
        if i < j:
            m = (i+j)//2
            self.merge_sort(li,i, m)
            self.merge_sort(li,m+1,j)
            self.merge(li, i, m, j)
              
    
    def reversePairs(self, nums: List[int]) -> int:
        #couting inversion logic
        self.count = 0
        self.merge_sort(nums, 0, len(nums)-1)
        return self.count
