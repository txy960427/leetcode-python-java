###1、暴力3836 ms，14.1 MB

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        elif len(s)==1:
            return 1
        else:
            last_number = 0
            i = 0
            while(i<len(s)):
                print(i)
                max_number = 1
                for j in range(i + 1, len(s) + 1):
                    if j < len(s) and s[j] not in s[i:j]:
                        max_number += 1
                    else:
                        if j < len(s):
                            next_index = s[i:j].index(s[j])+1+i
                            i = next_index
                        else:
                            i+=1
                        break

                if max_number > last_number:
                    last_number = max_number
           # print(last_number)
            return last_number
