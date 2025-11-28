class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=[]
        temp=''
        plus=0
        for i in digits:
            temp+=str(i)
        plus=int(temp)+1
        added_array=str(plus)
        for i in added_array:
            result.append(int(i))
        return result