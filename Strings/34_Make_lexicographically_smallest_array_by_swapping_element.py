class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = sorted((value, index) for index, value in enumerate(nums))

        result = nums[:]

        start = 0

        while start < n:
            end = start

            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            indices = sorted(arr[i][1] for i in range(start, end + 1))
            values = [arr[i][0] for i in range(start, end + 1)]

            for idx, value in zip(indices, values):
                result[idx] = value

            start = end + 1

        return result