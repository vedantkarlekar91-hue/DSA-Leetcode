class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        arr = []
        n = len(needle)
        for i in range(0,len(haystack)):
            result = haystack[i:i+n]
            arr.append(result)
        
        for i in range(len(arr)):
            if arr[i] == needle:
                return i
        return -1