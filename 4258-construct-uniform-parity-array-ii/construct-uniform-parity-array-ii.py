class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        odd=float('inf')
        even=float('inf')

        for i in nums1:
            if i%2==0:
                even=min(even,i)
            else:
                odd=min(odd,i)

        if even!=float('inf') and odd!=float('inf'):
            if even<odd:
                return False
        return True