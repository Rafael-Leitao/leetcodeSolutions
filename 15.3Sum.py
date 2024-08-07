"""
    -   My idea here is to create three pointer to iterate the array.
    -   Then I will store then sorted so that next time I get a valid solution
        I can check if the sorted solution is not already in my returned array.
        If it is there, then I don't add to it.
"""

    def threeSum(nums):
        left, right = 0, len(nums) - 1
        arr = []

        while left < right:
            mid = left + 1
            while mid < right:
                currentSum = nums[left] + nums[mid] + nums[right]
                if ( currentSum == 0):
                    temp = [nums[left], nums[mid], nums[right]].sort
                    if temp not in arr:
                        arr.append(temp)
                mid += 1
            right -= 1

