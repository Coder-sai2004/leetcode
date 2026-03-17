class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        #freq to check current frequency of each value
        # s=current_sum , l=length of curr sub array , i and j for indexing , mi for final minimum answer 
        freq={}
        s,i,j,l=0,0,0,0
        mi=float('inf')

        while j<len(nums):
            # if the val not in freq, we just increase the l and freq count of that val, and add val to the s
            if nums[j] not in freq or freq[nums[j]]==0:
                s+=nums[j]
                l+=1
                freq[nums[j]]=freq.get(nums[j],0)+1

            # if the val in freq, we just increase the length of sub_array and freq count of that val
            elif nums[j] in freq:
                freq[nums[j]]=freq.get(nums[j],0)+1
                l+=1

            #if sum greater than or equal to k, we adjust the subarray according to that    
            while s>=k:
                mi=min(mi,l)
                if freq[nums[i]]==1:
                    s-=nums[i]
                    freq[nums[i]]=freq.get(nums[i],0)-1
                    l-=1
                elif freq[nums[i]]>1:
                    l-=1
                    freq[nums[i]]=freq.get(nums[i],0)-1
                i+=1
            j+=1
        if mi>len(nums):
            return -1
        return mi