# Dec 1,2021
# Problem statement - Given a string S. The task is to convert characters of string to lowercase.

class Solution:
    def toLower(ob, S):
        #easy way
        return S.lower()
        #Another way
        for char in S:
            if char.isupper():
                low_char = char.lower()
                S = S.replace(char,low_char)
        return S


# code here

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.toLower(S))
# } Driver Code Ends

#Note - what does that 'for _ in range()' - https://stackoverflow.com/questions/66425508/what-is-the-meaning-of-for-in-range
