class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potSols = {target - num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if num in potSols and not i == potSols[num]:
                return [i, potSols[num]]
        
            