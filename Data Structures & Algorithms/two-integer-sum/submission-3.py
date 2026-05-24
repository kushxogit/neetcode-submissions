class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_of_indices = {}
        for i in range(len(nums)):
            current_number = nums[i] 
            required_number = target - current_number

            if required_number in map_of_indices:
                return [map_of_indices[required_number], i]

            map_of_indices[current_number] = i


