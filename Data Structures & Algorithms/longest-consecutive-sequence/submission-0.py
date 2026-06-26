class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n_set = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in n_set:
                curr_length = 0
                while (n+curr_length) in n_set:
                    curr_length +=1
                longest = max(curr_length, longest)

        return longest





        