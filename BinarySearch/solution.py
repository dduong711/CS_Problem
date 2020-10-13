class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        mid = len(nums)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            index = self.search(nums[:mid], target)
            return index if index != -1 else index
        else:
            index = self.search(nums[mid+1:], target)
            return index + mid + 1 if index != -1 else index
