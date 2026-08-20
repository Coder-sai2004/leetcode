class Solution: 
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int: 
        # left and right store the left_side and right_side of booked seats for each row
        # ans stores the total number of 4-person groups that can be assigned
        # seats_booked_rows stores rows with at least one booked seat
        # seats_not_booked_rows stores rows with no booked seats
        left = {} 
        right = {} 
        ans = 0 
        seats_booked_rows = set() 
        seats_not_booked_rows = 0 
        total_rows=n
 
        for x in reservedSeats: 
            row=x[0] 
            seat=x[1] 
            seats_booked_rows.add(row) 
 
            # Store the maximum booked seat on the left_side (seats 1-5) for each row
            if 1<=seat<=5: 
                if row in left: 
                    left[row]=max(left[row],seat) 
                else: 
                    left[row]=seat 
 
            # Store the minimum booked seat on the right_side (seats 6-10) for each row
            elif 6<=seat<=10: 
                if row in right: 
                    right[row]=min(right[row],seat) 
                else: 
                    right[row]=seat 
         
        # Check only rows with at least one booked seat for available 4-person groups
        for row in seats_booked_rows: 
            # Default booked boundaries when no seat is booked on either side
            left_booked=1 
            right_booked=10 
 
            # Update left_booked and right_booked using the actual booked seats
            if row in left: 
                left_booked=left[row] 
             
            if row in right: 
                right_booked=right[row] 

            # Calculate available seats between the left_side and right_side booked seats
            available=(right_booked-1)-left_booked 

            # Check whether the available seats can fit one or more 4-person groups
            if (available==4 and (left_booked!=2 and left_booked!=4 and left_booked!=6)) or available>4: 
                ans+=available//4 
 
        # Every completely unbooked row can fit two 4-person groups
        seats_not_booked_rows=(total_rows-len(seats_booked_rows))*2 
 
        return ans+seats_not_booked_rows