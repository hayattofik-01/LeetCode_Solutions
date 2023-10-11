class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if ':' in queryIP:
            ip = queryIP.split(':')
            if len(ip) != 8:
                return "Neither"
            
            for i in ip:
                if len(i) > 4 or len(i) < 1 :
                    return 'Neither'
                
                for j in i:
                    
                    if  (j.isalpha() and (ord(j.lower()) - ord('a'))) >= 6:
                        return "Neither"
            return "IPv6"
        else:
            ip = queryIP.split('.')
            
            if len(ip) != 4:
                return "Neither"
            
            
                                                    
                                                    
            for j in ip:
        
                if  not j or len(j) > 1 and  j[0] == "0":
                        return "Neither"
                    
                
                if j > "255" or len(j) > 3:
                    return 'Neither'
                for i in j:
            
                    if not i.isnumeric():
                            return "Neither"
            return "IPv4"
                    
                                     
                                      
        