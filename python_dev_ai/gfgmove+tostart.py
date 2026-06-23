class Solution:
    def segregateElements(self, arr):
        pos = []
        neg = []
        
        for i in range(len(arr)):
            if arr[i] >= 0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        arr[:] = pos + neg
        