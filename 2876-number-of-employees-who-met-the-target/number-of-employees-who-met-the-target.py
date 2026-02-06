class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for hour in hours:
            if hour>=target:
                c+=1
        return c