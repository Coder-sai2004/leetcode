class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total_cost = 0
        combined_cost = cost1 + cost2
        both_cost = costBoth

        # When item 1 is needed less
        if need1 < need2:
            total_cost += need1 * min(combined_cost, both_cost)

            extra = need2 - need1
            total_cost += extra * min((combined_cost - cost1), both_cost)
            
        # When item 2 is needed less
        elif need2 < need1:
            total_cost += need2 * min(combined_cost, both_cost)

            extra = need1 - need2
            total_cost += extra * min((combined_cost - cost2), both_cost)

        # When both requirements are equal
        else:
            total_cost += need1 * min(combined_cost, both_cost)

        return total_cost