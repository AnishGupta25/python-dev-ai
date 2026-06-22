class Solution:
    def sort012(self, arr):
        i , j , k = 0 , 0 , len(arr) - 1
        
        while j <= k:
            if arr[j] == 1:
                j += 1
            elif arr[j] == 0:
                arr[i] , arr[j] = arr[j] , arr[i]
                i += 1
                j += 1
            else:
                arr[k] , arr[j] = arr[j] , arr[k]
                k -= 1