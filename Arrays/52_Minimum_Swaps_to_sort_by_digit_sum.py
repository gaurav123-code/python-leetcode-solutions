
class Solution(object):
    def minSwaps(self, nums):
        def digit_sum(n):
            total = 0

            while n > 0:
                total += n % 10
                n //= 10

            return total

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        position = {num: i for i, num in enumerate(nums)}
        swaps = 0

        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                j = position[sorted_nums[i]]

                position[nums[i]] = j
                position[nums[j]] = i

                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1

        return swaps
