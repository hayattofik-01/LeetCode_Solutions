class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # dfs and backtracking
        self.s = s
        self.len_s = len(s)
        self.ans = []

        self.dfs(0, [])

        return self.ans

    def dfs(self, index, partition):
        if index == self.len_s:
            # we reached the end of the string
            if len(partition) == 4:
                self.ans.append(".".join(partition))
            return
        
        if index < self.len_s and len(partition) == 4:
            # we haven't used all the characters to build 4 address fields
            return

        if self.s[index] == '0':
            partition.append('0')
            self.dfs(index + 1, partition)
            partition.pop()
        else:
            for i in range(index + 1, self.len_s + 1):
                if 0 <= int(self.s[index: i]) <= 255:
                    partition.append(self.s[index: i])
                    self.dfs(i, partition)
                    partition.pop()
                else:
                    # no need to check further as the value is not in the range of 0 ~ 255
                    break