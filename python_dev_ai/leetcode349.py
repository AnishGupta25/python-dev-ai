class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = j = 0
        ans = set()
        nums1.sort()
        nums2.sort()

        while (i < len(nums1) and j < len(nums2)):
            if(nums1[i] == nums2[j]):
                ans.add(nums1[i])
                i += 1
                j += 1
            else:
                if(nums1[i] < nums2[j]):
                    i += 1
                else:
                    j += 1
        
        return list(ans)
    

class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))