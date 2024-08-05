class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1 for i in range(len(nums))]
        pre, pos = 1, 1

        for b in range(len(nums)):
            answer[b] *= pre
            pre *= nums[b]

        for c in range(len(nums) - 1, -1, -1):
            answer[c] *= pos
            pos *= nums[c]

        return answer

a = Solution()

nums = [1,2,3,4]
#nums = [-1,1,0,-3,3]
print("This is the solution:\n", a.productExceptSelf(nums))

