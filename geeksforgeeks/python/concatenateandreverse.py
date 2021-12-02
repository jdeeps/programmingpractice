# Dec 2,2021
# Problem statement -
# { Given two strings S1 and S2 as input. Your task is to concatenate two strings and then reverse the string.
# Finally print the reversed string. }

class Solution:
    def conRevstr (ob, S1, S2):
        S3 = S1 + S2
        print("Concatenated string is ",S3)
        str_arr = []
        for char in S3:
            if(char == ' '):
                continue
            str_arr.append(char)
        i = -1
        reversed_str = ''
        while i > -(len(str_arr) + 1):
            reversed_str += str_arr[i]
            i= i - 1
        return reversed_str

#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        S1 = input()
        S2 = input()
        ob = Solution()
        print(ob.conRevstr(S1,S2))
# } Driver Code Ends
