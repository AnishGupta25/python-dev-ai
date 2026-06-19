#User function Template for python3

class Solution:
    def roundToNearest (self, s) : 
        last = int(s[-1])

        if last <= 5:
            return s[:-1] + '0'

        num = list(s)

        num[-1] = '0'

        i = len(num) - 2

        while i >= 0 and num[i] == '9':
            num[i] = '0'
            i -= 1

        if i >= 0:
            num[i] = str(int(num[i]) + 1)
            return ''.join(num)

        return '1' + ''.join(num)