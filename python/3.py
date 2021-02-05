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
        
#2、滑动窗口 72ms

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
            windows = []
            last_number = 0
            for ss in s:
                if ss not in windows:
                    windows.append(ss)
                else:
                    windows = windows[windows.index(ss) + 1:]
                    windows.append(ss)
                last_number = max(last_number,len(windows))
            print(last_number)
            return last_number
        
#3、双指针


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
            left,right = 0,0
            last_number = 0
            for i,ss in enumerate(s):
                if ss not in s[left:right]:
                    right+=1
                else:
                    left += s[left:right].index(ss) + 1
                    right+=1
                last_number = max(right-left,last_number)
            print(last_number)
            return last_number
