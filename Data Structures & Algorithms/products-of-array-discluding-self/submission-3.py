class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        list1 =[]
        list2 = []
        for item in nums:
            product = product * item
            list1.append(product)
        product = 1 
        for i in range(len(nums)):
            product = product * nums[len(nums)-1-i]
            list2.append(product)
        list2.reverse()
        output = []
        for i in range(len(nums)):
            if i == 0:
                temp = list2[1]
            elif i == len(nums)-1:
                temp = list1[len(nums)-2]
            else:
                temp = list1[i-1] * list2[i+1]
            output.append(int(temp))
        return output
    