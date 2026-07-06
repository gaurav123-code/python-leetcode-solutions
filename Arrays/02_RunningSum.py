class Solution:
    def runningSum(self, nums):
        running_sum = []
        total = 0

        for number in nums:
            total = total + number
            running_sum.append(total)

        return running_sum