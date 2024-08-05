class Solution:

    def groupAnagrams(self, strs):
        mp = {}
        ans = []

        for s in strs:
            sorted_str = "".join(sorted(s))
            print("This is the sorted_str: \n", sorted_str)

            if sorted_str in mp:
                ans[mp[sorted_str]].append(s)
                print("This is in the if statement: \n",  ans)
            else:
                mp[sorted_str] = len(ans)
                ans.append([s])
                print("This is in the array: \n", ans)
                print("This is in the hashMap: \n", mp)

        return ans


a = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print("This is the solution: \n", a.groupAnagrams(strs))
