class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for i in nums:
            if temp.get(i):
                return True
            else:
                temp[i]=1
        return False
        