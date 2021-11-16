class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ### Two-line solution
        potSols = {target - num: i for i, num in enumerate(nums)}
        return next([i, x] for i, num in enumerate(nums) if (x := potSols.get(num)) and i != x)
        
        ### Most memory-efficient solution
        # potSols = {target - num: i for i, num in enumerate(nums)}
        # for i, num in enumerate(nums):
        #     if num in potSols and not i == potSols[num]:
        #         return [i, potSols[num]]