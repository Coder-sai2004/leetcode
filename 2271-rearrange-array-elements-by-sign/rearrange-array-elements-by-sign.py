class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        arranged=[]
        for i in nums:
            if i<0:
                negative.append(i)
            else:
                positive.append(i)
        for i in range(len(positive)):
            arranged.append(positive[i])
            arranged.append(negative[i])
        return arranged