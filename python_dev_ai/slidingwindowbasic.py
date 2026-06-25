class Solution:
    def maxSubarraySum(self, arr, k):
        wSum = sum(arr[:k])
        maxSum = wSum
        l = 0 
        for r in range(k, len(arr)):
            wSum -= arr[l]
            wSum += arr[r]
            l += 1
            maxSum = max(maxSum , wSum)
        return maxSum