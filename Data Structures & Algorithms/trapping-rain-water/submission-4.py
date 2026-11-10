class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        maxleft = []
        maxright = []
        current = 0
        for i in range(len(height)):
            if i == 0:
                maxleft.append(height[i])
            else:
                current = height[i]
                maxleft.append(max(current, maxleft[i-1]))

        height.reverse()
        for i in range(len(height)):
            if i == 0:
                maxright.append(height[i])
            else:
                current = height[i]
                maxright.append(max(current, maxright[i-1]))
        height.reverse()
        maxright.reverse()


        for i in range(len(height)):
            if (i == (len(height)-1)):
                return volume
            crevice = (min(maxleft[i], maxright[i]) - height[i])
            if (crevice < 0) or (i == 0):
                crevice = 0
            volume = volume + crevice
