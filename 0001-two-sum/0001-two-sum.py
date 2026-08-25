class Solution:
    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):
            current_number = nums[i]

            needed = target - current_number

            if needed in seen:
                return [seen[needed], i]
            seen[current_number] = i

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna