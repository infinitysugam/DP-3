# We solve this using DP.
# Time Complexity = O(n)
# Space Complexity = O(max(n))
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if  not nums:
            return 0

        freq = [0] * (max(nums)+1)
        for n in nums:
            freq[n] += n

        dp = [0] * len(freq)
        dp[1] = freq[1]
        for i in range(2, len(freq)):
            dp[i] = max(freq[i] + dp[i-2], dp[i-1])

        return dp[len(freq)-1]

