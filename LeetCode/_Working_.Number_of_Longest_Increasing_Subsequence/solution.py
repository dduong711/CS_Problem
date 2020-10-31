# solution.py

# -> Submission Result: Time Limit Exceeded

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        arr = [[0]*len(nums) for _ in nums]
        res = len(nums)
        for i in range(len(arr)):
            arr[i][i] = 1
        for L in range(2, len(nums)+1):
            n_arr = [[0]*len(nums) for _ in nums]
            for i in range(len(nums)-L+2-1):
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        n_arr[i][j] = sum(arr[j])
            arr = n_arr
            if self.sum_matrix(arr) != 0:
                res = self.sum_matrix(arr)
        return res

    def sum_matrix(self, matrix):
        return sum([sum(r) for r in matrix])
        
