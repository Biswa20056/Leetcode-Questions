class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n*(n+1)//2
        arr_sum = 0
        for num in nums:
            arr_sum+=num
        return total_sum - arr_sum

        