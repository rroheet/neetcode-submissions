class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        res = sorted(counter, key=lambda x: counter[x])[::-1]
        return res[:k]
        