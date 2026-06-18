#User function Template for python3
class Solution:
    def rotate(self, arr):
        
        i = len(arr) - 1
        last = arr[-1]
        
        while(i > 0):
            arr[i] = arr[i - 1]
            i -= 1
            
        arr[0] = last