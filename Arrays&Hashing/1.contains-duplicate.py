#On 10/27/23
# 217. Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = list()
        for i in nums:
            if i in x:
                return True
            else:
                x.append(i)
        return False
