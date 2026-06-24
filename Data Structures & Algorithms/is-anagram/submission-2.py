class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        if len(s)!=len(t):
            return False
        
        for n in range(len(s)):
            s_map[s[n]] +=1
            t_map[t[n]] +=1
        return s_map == t_map

        

        