class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr = list(set(arr))
        if len(set(arr)) == 1: return -1
        else:
            arr.remove(max(arr))
            return max(arr)