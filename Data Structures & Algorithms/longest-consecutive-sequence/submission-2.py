class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        currentLen = 1
        maxLen = 1
        if nums == []:
            return 0
        if len(nums) ==1:
            return 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                currentLen += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                currentLen = 1
            if maxLen < currentLen:
                maxLen = currentLen
        return maxLen