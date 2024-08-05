from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashMap = defaultdict(int)

        ret = []

        for i in range(len(nums)):
            hashMap[nums[i]] += 1

        for key in hashMap:
            if hashMap[key] >= max(hashMap.values()):
                ret.append(key)
                hashMap[key] -= min(hashMap.values())
                if len(ret) > k:
                    break
        return ret

        # numMap = {}
        #
        # for number in nums:
        #     if number not in numMap:
        #         numMap[number] = 1
        #     else:
        #         numMap[number] += 1
        #
        #
        #
        # arr = []
        #
        # for i in range(0, k):
        #     maxValue = max(numMap.values())  # 2
        #
        #     for key, value in numMap.items():
        #         if value == maxValue:
        #             arr.append(key)
        #             numMap[key] = 0
        #             maxValue += 1
        #
        #
        # return arr

        """
        class Solution(object):
    def topKFrequent(self, nums, k):
        numMap = {}
        arr = [ [] for i in range(len(nums) + 1)]

        for number in nums:
            numMap[number] = 1 + numMap.get(number, 0)
        
        for key, value in numMap.items():
            arr[value].append(key)

        res = []

        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
                    
    """

a = Solution()

nums = [1,1,1,2,2,3]
k = 1


print("This is the final result: \n", a.topKFrequent(nums, k))