class Solution:
    def defangIPaddr(self, address: str) -> str:
        newstr=address.replace(".","[.]")
        return newstr