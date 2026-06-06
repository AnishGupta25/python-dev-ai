class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        if not nums: return []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i+1] = 0

        result = []

        for num in nums:
            if num != 0:
                result.append(num)

        while len(result) < len(nums):
            result.append(0)

        return result
        

class Solution2:
    def applyOperations(self, nums: List[int]) -> List[int]:
        if not nums: return []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i+1] = 0

        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        while j < len(nums):
            nums[j] = 0
            j += 1

        return nums