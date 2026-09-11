from math import comb

class Solution:
    def getProbability(self, balls):

        n = sum(balls) // 2

        dp = {(0, 0, 0): 1.0}

        for balls_count in balls:

            new_dp = {}

            for (used, distinct1, distinct2), ways in dp.items():

                for x in range(balls_count + 1):

                    new_used = used + x

                    if new_used > n:
                        continue

                    new_distinct1 = distinct1
                    new_distinct2 = distinct2

                    if x > 0:
                        new_distinct1 += 1

                    if x < balls_count:
                        new_distinct2 += 1

                    state = (
                        new_used,
                        new_distinct1,
                        new_distinct2
                    )

                    new_dp[state] = (
                        new_dp.get(state, 0)
                        + ways * comb(balls_count, x)
                    )

            dp = new_dp

        good = 0
        total = 0

        for (used, distinct1, distinct2), ways in dp.items():

            if used == n:

                total += ways

                if distinct1 == distinct2:
                    good += ways

        return good / total