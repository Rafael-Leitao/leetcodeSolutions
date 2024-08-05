class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        for i in nums:
            if i not in num_set:
                num_set.add(i)
            else:
                return True
        return False


a = Solution()
nums = [1,2,3,1]
print("The solution is: \n", a.containsDuplicate(nums))

'''Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true'''