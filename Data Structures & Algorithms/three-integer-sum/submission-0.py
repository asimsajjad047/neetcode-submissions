class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            print(nums[i], i)
        for i in range(len(nums)):
            for j in range(len(nums)):
                need = 0 - nums[i] - nums[j]
                if (need in hashmap) and (hashmap[need]!= i) and (i != j) and (j != hashmap[need]):
                    into = [nums[i], nums[j], need]
                    into.sort()
                    if into not in triplets:
                        print(nums[i], nums[j], need, i, j, hashmap[need])
                        triplets.append(into)

        return(triplets)