class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow_freq = {}
        con_freq = {}
        for i in range(len(s)):
            if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
                if s[i] in vow_freq:
                    vow_freq[s[i]] += 1
                else:
                    vow_freq[s[i]] = 1

            else:
                if s[i] in con_freq:
                    con_freq[s[i]] += 1
                else:
                    con_freq[s[i]] = 1
        if vow_freq:
            max_vow = max(vow_freq.values())
        else:
            max_vow = 0

        if con_freq:
            max_con = max(con_freq.values())
        else:
            max_con = 0

        result = max_vow + max_con
        return result