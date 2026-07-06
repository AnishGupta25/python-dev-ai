class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes , idx , prod = 0 , -1 , 1

        for i in range(len(nums)):
            if nums[i] == 0: 
                zeroes += 1
                idx = i
            else: prod *= nums[i]
        
        if zeroes == 0:
            for i in range(len(nums)):
                nums[i] = prod // nums[i]
        elif zeroes == 1:
            for i in range(len(nums)):
                nums[i] = 0
            nums[idx] = prod
        else:
            for i in range(len(nums)):
                nums[i] =  0
        return nums