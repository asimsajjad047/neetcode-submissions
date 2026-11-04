class Solution:
    def isPalindrome(self, s: str) -> bool:
        point1 = 0
        point2 = int(len(s)) -1
        s = s.lower()
        while point1 < point2:
            print(point1, point2)
            if s[point1].isalnum() == False:
                point1 +=1
                continue
            if s[point2].isalnum() == False:
                point2 -= 1
                continue
            if s[point1] != s[point2]:
                print(point1, point2)
                return False
            else:
                point1 += 1
                point2 -= 1
        return True