class Solution: 
    def twoSum (self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for current_index, current_val in enumerate(nums):
            complement = target - current_val

            if complement in seen:
                return [seen[complement], current_index]
            
            seen[current_val] = current_index
        return []