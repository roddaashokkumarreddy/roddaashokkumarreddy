from collections import defaultdict
class Solution(object):
    def longestWord(self, words):
        seen, res = set(['']), ""
        buckets = defaultdict(set)
        min_len, max_len = float('inf'), float('-inf')
        for w in words:
            buckets[len(w)].add(w)
            min_len, max_len = min(min_len, len(w)), max(max_len, len(w))
        for l in range(min_len, max_len+1):
            for w in buckets[l]:
                if w[:-1] in seen:
                    seen.add(w)
                    if len(w) > len(res) or (len(w) == len(res) and res > w):
                        res = w
        return res

words = ["a","banana","app","appl","ap","apply","apple"]
obj1 = Solution()
print("The Longest Word:",obj1.longestWord(words))







