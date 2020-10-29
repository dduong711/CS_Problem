# solution.py

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        s = "".join(list(map(str, seats))).split("1")
        d = list(map(lambda s_: len(s_)//2 + len(s_)%2, s))
        if seats[0] == 0:
            d[0] = len(s[0])
        if seats[-1] == 0:
            d[-1] = len(s[-1])
        return max(d)
