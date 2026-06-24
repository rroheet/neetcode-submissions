class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        # store the counts
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        # bucket sort
        freq = [[] for i in range(len(nums)+1)]

        for n, count in counts.items():
            freq[count].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
