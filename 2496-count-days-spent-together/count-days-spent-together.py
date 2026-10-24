class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Number of days in each month (non-leap year)
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Cumulative days up to the end of each month
        pre = [days[0]]

        for i in range(1, len(days)):
            pre.append(pre[i - 1] + days[i])

        # Combine arrival and departure dates of Alice and Bob
        alice = arriveAlice.split('-') + leaveAlice.split('-')
        bob = arriveBob.split('-') + leaveBob.split('-')

        # Convert date strings into integers
        alice = [int(i) for i in alice]
        bob = [int(i) for i in bob]

        # a1 = Alice's arrival day number
        # a2 = Alice's departure day number
        # b1 = Bob's arrival day number
        # b2 = Bob's departure day number
        a1 = pre[alice[0] - 1] + alice[1]
        a2 = pre[alice[2] - 1] + alice[3]
        b1 = pre[bob[0] - 1] + bob[1]
        b2 = pre[bob[2] - 1] + bob[3]

        print(a1,a2,b1,b2)

        # Count the days both Alice and Bob are present
        ans = 0

        for i in range(b1, b2 + 1):
            if i >= a1 and i <= a2:
                ans += 1

        return ans