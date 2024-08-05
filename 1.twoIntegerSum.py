class Solution():

    def twoSum(self, nums, target):

        '''

        This is the brute force:: O(n^2)

        :param nums:
        :param target:
        :return:

        arrayLength = len(nums)

        if arrayLength < 2 or target is None:
            return False

        for i in range(arrayLength - 1):
            for j in range(i + 1, arrayLength):


                if nums[i] + nums[j] == target:
                    return i, j

        return False

'''

        # This is the solution using a hash table, the time complexity is O(n).

class Solution():

    def twoSum(self, nums, target):

        numMap = {}
        n = len(nums)

        # Init the hash table:
        for i in range(n):
            numMap[nums[i]] = i
            print("This is the numMap: \n", numMap)

        #Find the complement:
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return []   #No solution








a = Solution()
arr = [2, 7, 11, 14]
target = 9

print("This is the solution: \n", a.twoSum(arr, target))
