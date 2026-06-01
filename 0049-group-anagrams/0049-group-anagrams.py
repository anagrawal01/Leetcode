class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        i= 0
        while i<len(strs):
            sorted_strs = ''.join(sorted(strs[i]))
            if sorted_strs not in groups:
                groups[sorted_strs] = []
            groups[sorted_strs].append(strs[i])
            i+=1
        return list(groups.values())