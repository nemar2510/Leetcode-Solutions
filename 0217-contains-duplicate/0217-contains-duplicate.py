class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_index=set()
        for i in range(len(nums)):
            if nums[i] in last_index:
                return True
            last_index.add(nums[i])
        return False