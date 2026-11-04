class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        restList = {}
        for i in range(len(numbers)):
            restList[numbers[i]] = i

        for i in range(len(numbers)):
            need = target - numbers[i]
            if need in restList and restList[need] != i:
                return [i + 1, restList[need] + 1]