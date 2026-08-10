class Solution:
    def water(self, height,index):
        idx=index
        res = 0
        val = 0

        left = 0
        right = 1

        # Traverse until the tallest bar.
        while right <= idx:
            # Keep accumulating heights until a taller/equal bar is found.
            if height[left] > height[right]:
                val += height[right]
                right += 1

            # A valid right boundary is found.
            elif height[left] <= height[right]:

                # Width between the two boundary bars.
                width = (right - left) - 1

                # Rectangle area formed by the left boundary.
                area = height[left] * width

                # Water trapped inside the current section.
                trapped_water = area - val

                res += trapped_water
                val = 0

                # Move to the next section.
                left = right
                right += 1
        return res

    def trap(self, height: List[int]) -> int:
        temp = height[::-1]
        # Find the tallest bar and its index from both sides.
        mx = max(height)
        idx = height.index(mx)
        r_idx=len(temp)-idx-1
        
        left_half = self.water(height,idx)
        right_half = self.water(temp,r_idx)

        return left_half + right_half