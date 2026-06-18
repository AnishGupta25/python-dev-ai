#User function Template for python3

# function for adding one to number 
class Solution:
    # Function to add one to a number represented as an array
    def addOne(self, arr):
        # code here
        arr.reverse()
        i = 0
        carry = 1
        while i < len(arr) and carry:
            arr[i] += carry
            carry = arr[i] // 10 
            arr[i] %= 10
            i += 1
            
        if carry: arr.append(carry)
        
        arr.reverse()
        
        return arr