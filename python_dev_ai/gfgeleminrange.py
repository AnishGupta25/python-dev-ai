class Solution:
    def checkElements(self, start, end, arr):
        if start > end : return False
        arr_set = set(arr)
        
        for i in range(start , end + 1):
            if i not in arr_set: return False
            
        return True
        