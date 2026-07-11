class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {key: -1 for key in nums2}
        ans = [-1]*(len(nums1))
        for i in range (len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                d[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        for i in range (0, len(nums1)):
            ans[i] = d[nums1[i]]   
        return ans             
        