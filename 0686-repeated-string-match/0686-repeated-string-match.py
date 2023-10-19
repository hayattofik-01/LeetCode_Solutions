class Solution:
                
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == b: return 1
        
        # return if a doesnt contain all unique characters of b even once
        char_a = set()
        for s in a:
            if s not in char_a: char_a.add(s)
        
        for t in b:
            if t not in char_a: return -1
            
        org_a = a
        repeat = 1
        n = len(b)
        
        # calculate pi for KMP
        pi = [0 for _ in range(n)]
        j = 0
        for i in range(1, n):
            while j and b[i] != b[j]:
                j = pi[j-1]
            j += (b[i] == b[j])
            pi[i] = j
        
        # a should be atleast of length b
        while len(a) < len(b):
            a += org_a
            repeat += 1
        
        # KMP string search
        def strStr(s, t, pi):
            i = 0; j = 0
            while i < len(s):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                    if j == len(t): return True
                elif j > 0: j = pi[j-1]
                else: i += 1
            return False
    
        # keep looking until len(a) <= 2 * len(b)
        found = strStr(a, b, pi)
        while not found:
            if repeat == 1 or len(a) <= 2 * len(b):
                a += org_a
                repeat += 1
                found = strStr(a, b, pi)
                continue
            else: break
                
        return repeat if found else -1