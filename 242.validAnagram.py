class Solution(object):
    def isAnagram(self, s, t):

        if s is None or t is None or (len(s) != len(t)):
            return False

        listT = []

        for i in t:
            listT.append(i)

        for letter in s:
            if letter in listT:
                listT.remove(letter)

        if len(listT) == 0:
            return True

        else:
            return False


a = Solution()
s = "anagram"
t = "nagaram"

print("This is the solution: \n", a.isAnagram(s, t))