class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for p in range(len(nums)):
                if nums[i] + nums[p] == target and i != p:
                    return[min(i, p), max(i, p)]