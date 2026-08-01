class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        left = 0
        count = defaultdict(int)

        for right in range(len(fruits)):
            count[fruits[right]] += 1
            if len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            res = max(res, right - left + 1)
        return res



        