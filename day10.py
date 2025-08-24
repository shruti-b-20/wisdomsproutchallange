from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            dic[tuple(count)].append(word)
        return list(dic.values())


# -------- Test Cases --------
sol = Solution()

print("Input: strs = [\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"]")
print("Output:", sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\nInput: strs = [\"\"]")
print("Output:", sol.groupAnagrams([""]))

print("\nInput: strs = [\"a\"]")
print("Output:", sol.groupAnagrams(["a"]))

print("\nInput: strs = [\"abc\", \"bca\", \"cab\", \"xyz\", \"zyx\", \"yxz\"]")
print("Output:", sol.groupAnagrams(["abc", "bca", "cab", "xyz", "zyx", "yxz"]))

print("\nInput: strs = [\"abc\", \"def\", \"ghi\"]")
print("Output:", sol.groupAnagrams(["abc", "def", "ghi"]))
