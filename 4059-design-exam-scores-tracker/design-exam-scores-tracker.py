import bisect
class ExamTracker:
    def __init__(self):
        self.times = []
        self.prefix = [0]
        self.glavonitre = []

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.prefix.append(self.prefix[-1] + score)
        self.glavonitre.append((time, score))

    def totalScore(self, startTime: int, endTime: int) -> int:
         left = bisect.bisect_left(self.times, startTime)
         right = bisect.bisect_right(self.times, endTime) - 1
         if left > right:
             return 0
         return self.prefix[right + 1] - self.prefix[left]

# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)