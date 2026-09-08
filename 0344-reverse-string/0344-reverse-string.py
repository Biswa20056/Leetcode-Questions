class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st = 0
        l = len(s)-1
        end = l
        while st<end:
            s[st],s[end] = s[end],s[st]
            st+=1
            end-=1
        return s        