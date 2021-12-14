# -----------------------------------------------------------------------------------------------------------------------
# Date Dec 14,2021
# Problem statement :
# { Given a series 9, 33, 73, 129...  Find the n-th term of the series.}
# -------------------------------------------------------------------------------------------------------------------------

class Solution:
    def nthOfSeries(self, n):
        if n == 1:
            return 9
        else:
            seriesNum = 9
            for i in range(2, n + 1):
                # Calculation for the series happens like 9+(24+16*(n-i))
                # Here, 'i' will be all the numbers from 2 to n
                # For example, for n =3 - 9+(24+16*(3-2))+(24+16*(3-3)) = 73
                seriesNum += 24 + 16 * (n - i)
            return seriesNum


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.nthOfSeries(n))
# } Driver Code Ends
