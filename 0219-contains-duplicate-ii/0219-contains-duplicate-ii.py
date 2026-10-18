class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_index={}
        for i in range(len(nums)):
            if nums[i] in last_index:
                previous_index=last_index[nums[i]]
                if i-previous_index<=k:
                    return True
            last_index[nums[i]]=i
        return False