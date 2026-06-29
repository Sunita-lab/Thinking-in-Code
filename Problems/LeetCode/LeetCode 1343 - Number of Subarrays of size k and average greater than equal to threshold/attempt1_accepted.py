class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = sum(arr[:k])
        current_avg = current_sum/k
        

        count = 1 if current_avg >= threshold else 0

        for i in range (len(arr) - k):
            current_sum = current_sum - arr[i] + arr[i+k]
            current_avg = current_sum/k
            if current_avg >= threshold:
                count += 1
        return count        
        