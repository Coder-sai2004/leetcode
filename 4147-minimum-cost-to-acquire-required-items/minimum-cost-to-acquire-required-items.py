class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total = 0
        pair_cost = cost1 + cost2
        combo_cost = costBoth
        difference = abs(need1 - need2)

        # Cover common requirements
        total += min(need1, need2) * min(pair_cost, combo_cost)

        # Extra type 2 requirement
        if need1 < need2:
            total += difference * min(cost2, combo_cost)

        # Extra type 1 requirement
        if need2 < need1:
            total += difference * min(cost1, combo_cost)

        return total