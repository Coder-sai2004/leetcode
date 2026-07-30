class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        left = 0
        right = 0
        count = 0
        ans = 0

        while right < len(fruits):

            baskets[fruits[right]] = baskets.get(fruits[right], 0) + 1
            count += 1
            right += 1

            #if baskets contains more than 2 types of fruits then we sheink or delete fruits from left side
            while len(baskets.keys()) > 2:
                count -= 1
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1

            if len(baskets.keys()) == 2:
                ans = max(ans, count)

        ans = max(ans, count)
        return ans