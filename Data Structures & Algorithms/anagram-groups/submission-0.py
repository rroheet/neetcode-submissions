class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in hashmap:
                hashmap[s_sorted].append(s)
            else:
                hashmap[s_sorted] = [s]
        return list(hashmap.values())
        