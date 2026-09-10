class Solution:
    def soupServings(self, n: int) -> float:

        # 25 mL ko 1 unit maan lo
        n = (n + 24) // 25

        # Bahut bara n ho to answer practically 1 hota hai
        if n >= 179:
            return 1.0

        memo = {}

        def dp(a, b):

            # Dono soups ek hi turn mein khatam
            if a <= 0 and b <= 0:
                return 0.5

            # Sirf A khatam
            if a <= 0:
                return 1.0

            # Sirf B khatam
            if b <= 0:
                return 0.0

            # Agar pehle calculate kar chuke hain
            if (a, b) in memo:
                return memo[(a, b)]

            # 4 possible operations
            ans = (
                dp(a - 4, b)
                + dp(a - 3, b - 1)
                + dp(a - 2, b - 2)
                + dp(a - 1, b - 3)
            ) / 4

            # Result save kar do
            memo[(a, b)] = ans

            return ans

        return dp(n, n)
        