class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # left and right are the starting and ending indices.
        left = 0
        right = len(piles) - 1

        # turn indicates whose turn it is.
        turn = 0

        alice = 0
        bob = 0

        while left < right:
            # We consider the first and last piles along with their adjacent
            # piles to decide which pile gives the better next move.
            left_stone = piles[left]
            next_left = piles[left + 1]
            right_stone = piles[right]
            next_right = piles[right - 1]

            if turn % 2 == 0:
                if next_left < next_right:
                    alice += left_stone
                else:
                    alice += right_stone
            else:
                if next_left < next_right:
                    alice += left_stone
                else:
                    alice += right_stone

            left += 1
            right -= 1
            turn += 1

        if alice > bob:
            return True
        return False