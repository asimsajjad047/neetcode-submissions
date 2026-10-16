class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        found = {}
        for num in nums:
            if num not in found:
                found[num] = 1
            else:
                found[num] = 1 + found[num]

        output = []
        for i in range(k):
            max = 0
            mkey= 0
            for key, value in found.items():
                if value > max and key not in output:
                    max = value
                    mkey = key
            output.append(mkey)
        return (output)
