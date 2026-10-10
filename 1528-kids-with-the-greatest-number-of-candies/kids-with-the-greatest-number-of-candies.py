class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        max_candies = max(candies)

        result = []

        for candy in candies:
            if candy + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)



        return result
        