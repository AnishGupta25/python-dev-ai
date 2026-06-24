class Solution:
    def getMinDiff(self,arr,k):
        n = len(arr)

        if n <= 1:
            return 0

        arr.sort()

        ans = arr[n - 1] - arr[0]

        for i in range(1, n):

            small = min(arr[0] + k,
                        arr[i] - k)

            big = max(arr[n - 1] - k,
                      arr[i - 1] + k)

            ans = min(ans, big - small)

        return ans