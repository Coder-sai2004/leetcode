class Solution:
    def call(self,s):
        if len(s)==0:
            return False
        for i in s:
            if not i.isalnum() and i!='_':
                return False
        return True
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_coupon,temp_valid=[],[]
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        for j in range(len(code)):
            if self.call(code[j]) and businessLine[j] in order and isActive[j] is True:
                valid_coupon.append((businessLine[j],code[j]))     
        result=sorted(valid_coupon,key=lambda x: (order[x[0]], x[1]))
        final=[c for _,c in result]
        return final