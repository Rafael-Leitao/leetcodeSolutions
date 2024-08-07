"""
    -   My idea here is to create three pointer to iterate the array.
    -   Then I need to sort the list and create a set so that I can change that set to 
        a list and then return it.
    -   Then I will store then so that next time I get a valid solution
        I can check if the sorted solution is not already in my returned array.
        If it is there, then I don't add to it.
"""

def threeSum(nums):
    nums.sort()
    output = set()
    

    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + 1
        while mid < right:
            currentSum = nums[left] + nums[mid] + nums[right]
            print(currentSum)
            if currentSum < 0:
                mid += 1
            elif currentSum > 0:
                right -= 1
            else:
                output.add((nums[left], nums[mid], nums[right]))
                mid += 1
        left += 1
    
    return [list(triplet) for triplet in output]


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
