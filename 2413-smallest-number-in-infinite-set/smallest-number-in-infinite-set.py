class SmallestInfiniteSet:

    def __init__(self):
        self.s = set()
        for i in range(1,1001):
            self.s.add(i)

    def popSmallest(self) -> int:
        x = min(self.s)
        self.s.remove(x)
        return x

    def addBack(self, num: int) -> None:
        if num not in self.s:
            self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)