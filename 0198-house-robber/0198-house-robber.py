class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        money = [0] * (n + 1)
        money[1] = nums[0]

        for i in range(1, n):
            money[i + 1] = max(money[i], money[i - 1] + nums[i])

        return money[len(money) - 1]

        