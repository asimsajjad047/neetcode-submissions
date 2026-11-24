class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = [] # temp, index
        outStack = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while monoStack and t > monoStack[-1][0]:
                Ttemp, Tindex = monoStack.pop()
                outStack[Tindex] = (i-Tindex)

            monoStack.append((t, i))

        return outStack 