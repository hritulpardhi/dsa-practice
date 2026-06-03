class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for i in strs:
            key = ''.join(sorted(i))
            if temp.get(key):
                temp[key].append(i)
            else:
                temp[key] = [i]
        return list(temp.values())