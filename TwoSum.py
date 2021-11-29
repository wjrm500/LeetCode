from typing import List

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

### Testing
solution = Solution()
result1 = solution.twoSum([2, 7, 11, 15], 9)
result2 = solution.twoSum([3, 2, 4], 6)
result3 = solution.twoSum([3, 3], 6)
print(result1)
print(result2)
print(result3)

result4 = solution.twoSum([1, 3, 4, 2], 6)
print(result4)