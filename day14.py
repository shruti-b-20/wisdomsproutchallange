from collections import defaultdict

class Solution:
    def countExactlyK(self, s, k):
        def atMostK(s, k):
            n = len(s)
            freq = defaultdict(int)
            left = 0
            count = 0
            for right in range(n):
                freq[s[right]] += 1
                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
                count += right - left + 1
            return count

        return atMostK(s, k) - atMostK(s, k - 1)


sol = Solution()
print(sol.countExactlyK("pqpqs", 2))       # 7
print(sol.countExactlyK("aabacbebebe", 3)) # 10
print(sol.countExactlyK("a", 1))           # 1
print(sol.countExactlyK("abc", 3))         # 1
print(sol.countExactlyK("abc", 2))         # 2

        


