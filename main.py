class Solution:
    def longestCommonPrefix(self, strs):
        strs = [str]
    
        if len(strs) == 0:
            return ''
        res = ''
        strs = sorted(strs)
        for i in strs[0]:
            if strs[-1].startswith(res+i):
                res += i
            else:
                break
        return res

lonestCommonPrefix(strs['flow', 'flow', 'bruh'])