class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # initializations
        n = len(height)
        l = 0
        r = n-1
        level = 0
        water = 0
        # track from both sides
        while l < r:
            # pick the lower side and move
            if height[l] < height[r]:
                lower = height[l]
                l += 1
            else:
                lower = height[r]
                r -= 1
            # update level
            if lower > level:
                level = lower
            # accumulate water
            water += (level-lower)
        return water
