# solution.py

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        res = 0
        for i in range(1, len(s)+1):
            for j in range(len(s)+1-i):
                res += self.search(s[j:j+i], t)
        return res

    def search(self, s, t):
        arr = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(1, len(arr)):
            for j in range(1, len(arr[-1])):
                if s[i-1] != t[j-1]:
                    arr[i][j] = 1
                    if i > 1 and j > 1:
                        arr[i][j] += int(s[i-2] == t[j-2]) 
                else:
                    if i > 1 and j > 1:
                        arr[i][j] += int(s[i-2] != t[j-2]) 
        return sum([sum(r) for r in arr])
