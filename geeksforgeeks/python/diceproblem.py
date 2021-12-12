# -----------------------------------------------------------------------------------------------------------------------
# Date Dec 9,2021
# Problem statement :
# { You are given a cubic dice with 6 faces. All the individual faces have a number printed on them.
#  The numbers are in the range of 1 to 6, like any ordinary dice.
#  You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.}
# -------------------------------------------------------------------------------------------------------------------------
# THIS IS NOT A GOOD SOLUTION. I WILL COME UP WITH OTHER ONE.
class Solution:
    def oppositeFaceOfDice(self, N):
        if N == 1:
            return 6
        elif N == 2:
            return 5
        elif N == 3:
            return 4
        elif N == 4:
            return 3
        elif N == 5:
            return 2
        else:
            return 1


#{
#  Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)
# } Driver Code Ends
