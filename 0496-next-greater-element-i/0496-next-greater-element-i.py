class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        List1 = []

        for x in nums1: 
            found = False
            index = nums2.index(x)

            for j in range(index+1, len(nums2)):
                if nums2[j] > x:
                    List1.append(nums2[j])
                    found = True
                    break

            if not found:
                List1.append(-1)
        return List1