class Solution:
    def findTwoElement(self, arr):
        dub = missing = -1

        for i in range(len(arr)):
            val = abs(arr[i])

            if arr[val - 1] > 0:
                arr[val - 1] = -arr[val - 1]
            else:
                dub = val

        for i in range(len(arr)):
            if arr[i] > 0:
                missing = i + 1
                break

        return [dub, missing]