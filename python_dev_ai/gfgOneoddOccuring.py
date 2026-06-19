class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        ans = 0
        
        for i in range(len(arr)):
            ans = ans ^ arr[i]
            
        return ans