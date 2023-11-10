class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(int)
        check =[]
        for letter in s:
            counter[letter] +=  1
        buckets = [[] for freq in range(len(s) + 1)]
        
        for key in counter:
            buckets[counter[key]].append(key)
        output = ""
        for bucket in range(len(buckets) - 1, - 1, -1 ):
            for char in buckets[bucket]:
                output += bucket * char
        return output
                