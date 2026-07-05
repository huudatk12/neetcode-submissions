class Solution: 
    def twoSum (self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            emplement = target - num
            if emplement in seen:
                return [seen[emplement], i]
            seen[num] = i
        return