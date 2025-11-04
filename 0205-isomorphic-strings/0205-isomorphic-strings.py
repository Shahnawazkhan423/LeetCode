class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False

        map_st = {}
        map_ts = {}

        for ch_s, ch_t in zip(s, t):
            if ch_s in map_st and map_st[ch_s] != ch_t:
                return False
            if ch_t in map_ts and map_ts[ch_t] != ch_s:
                return False
            
            map_st[ch_s] = ch_t
            map_ts[ch_t] = ch_s

        return True