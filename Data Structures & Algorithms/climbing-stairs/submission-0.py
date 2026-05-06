class Solution:
    def climbStairs(self, n: int) -> int:
        iteration = 0
        first_step, next_step = 0, 1
        total = None

        while iteration < n:
            total = first_step + next_step

            first_step = next_step
            next_step = total

            iteration += 1
        
        return total