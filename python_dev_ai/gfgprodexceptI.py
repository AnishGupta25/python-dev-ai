class Solution:
    def productExceptSelf(self, arr):
        zeroes = 0
        idx = -1 
        product = 1
        
        for i in range(len(arr)):
            if arr[i] == 0:
                zeroes += 1
                idx = i
            else : product *= arr[i]
            
        if zeroes == 0:
            for i in range(len(arr)):
                arr[i] = product // arr[i]
                
        elif zeroes == 1:
            for i in range(len(arr)):
                arr[i] *= 0
            arr[idx] = product
            
        else:
            for i in range(len(arr)):
                arr[i] *= 0
                
        return arr 