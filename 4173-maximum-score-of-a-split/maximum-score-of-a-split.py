class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        nums_length=len(nums)
        #checking for length constraint
        if len(nums)<2:
            return 0
            
        #assigning prefix,suffix initial values
        prefix,suffix=[nums[0]],[0]*nums_length
        suffix[-1]=nums[-1]
        maximum_score=[]
        
        #calculating prefix
        for i in range(1,nums_length):
            prefix.append(prefix[i-1]+nums[i])
            
        #calculating suffix
        for i in range(nums_length-2,-1,-1):
            suffix[i]=(min(suffix[i+1],nums[i]))
            
        #calculating maximum score
        for i in range(nums_length-1):
            x=prefix[i]-suffix[i+1]
            maximum_score.append(x)
            
        return max(maximum_score)