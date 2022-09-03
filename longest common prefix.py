class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest = [strs[0]]
        if len(strs) > 1:
            for i in range(1,len(strs)):
                j = 0
                if longest[0] == "":
                    break
                inside = False
                for c in strs[i]:
                    if j < len(longest[0]) and c != longest[0][j]:
                        longest[0] = longest[0][:j]
                        inside = True
                        break
                    else:
                        j += 1
                if not inside and len(strs[i]) == 0:
                    longest[0] = ""
                else:             
                    if not inside and longest[0][0] == strs[i][0]:
                        longest[0] = longest[0][:j]
        return longest[0]