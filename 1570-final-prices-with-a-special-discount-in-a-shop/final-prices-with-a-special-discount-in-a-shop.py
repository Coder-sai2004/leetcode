class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        st = []

        res=[-1]*len(prices)
        for i in range(len(prices)):
            while st and prices[st[-1]]>=prices[i]:
                idx = st.pop()
                res[idx] = prices[i]

            st.append(i)
        
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = prices[i]
            else:
                res[i] = prices[i] - res[i]
        
        return res