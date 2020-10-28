class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        pre = nums[0]
        for i, _ in enumerate(nums):
            if i == len(nums)-1 or nums[i]+1 != nums[i+1]:
                if pre == nums[i]:
                    res.append(f"{nums[i]}")
                else:
                    res.append(f"{pre}->{nums[i]}")
                if i == len(nums)-1:
                    break
                pre = nums[i+1]
        return res