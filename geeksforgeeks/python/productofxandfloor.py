#Dec 4,2021
#Problem statement-
#{Given a positive integer n. Find the sum of product of x and y such that floor(n/x) = y .}

class Solution:
	def sumofproduct(self, n):
		pair_list = []
		for i in range(1,n+1):
			x = i
			y = int((n/x)).__floor__()
			t = (x,y)
			pair_list.append(t)
		if len(pair_list) > 0:
			sum = 0
			for i in range(0,len(pair_list)):
				tuple_item = pair_list[i]
				prod = tuple_item[0] * tuple_item[1]
				sum += prod
		return sum

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.sumofproduct(n)
		print(ans)
# } Driver Code Ends
