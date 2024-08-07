""" 
    -   So, my idea is to have two pointers, one starting at the beginning of the array
    and the second pointer starting at the end of array.
    -   Then while the left pointer is less then the right pointer, keep moving the pointer
    -   Possibly I will apply a binary search

"""

def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        currentSum = numbers[left] + numbers[right]
        if currentSum == target:
            return [left + 1, right + 1]
        elif currentSum < target:
            left += 1
        else:
            right -= 1


numbers = [-1, 0]
target = -1

print(twoSum(numbers, target))
