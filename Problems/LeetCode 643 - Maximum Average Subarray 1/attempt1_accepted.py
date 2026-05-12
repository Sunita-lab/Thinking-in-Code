class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = 0
        for i in range (k):
            current_sum += nums[i]
        max_avg  = current_sum/float(k) #float likhna jaruri hai python 2 me nahi to integer division ho jayega

        for i in range (len(nums) - k):
            current_sum = current_sum - nums[i] + nums[i+k]
            current_avg = current_sum/float(k)
            max_avg  = max(current_avg, max_avg)
        return max_avg
        
        
    