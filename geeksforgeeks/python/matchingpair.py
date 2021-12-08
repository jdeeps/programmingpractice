# -----------------------------------------------------------------------------------------------------------------------
# Date Dec 6,2021
# Problem statement :
# { Given a set of numbers from 1 to N, each number is exactly present twice so there are N pairs.
# In the worst-case scenario, how many numbers X should be picked and removed from the set until we find a matching pair? }
# -------------------------------------------------------------------------------------------------------------------------
class Solution:
    def find (self, N):
        # create a list with the elements ranging from 1 to N
        # example - for N=1, it will create a list {1} and then extend itself to create {1,1}
        list = []
        for i in range(1,N+1):
            list.append(i)
        list.extend(list)
        # following lines of code will iterate 'list' and simultaneously add it to 'matching_list'.
        # If the same element is found in the 'matching_list' then it will return the number of times it picked to get a matching pair
        matching_list =[]
        for i in range(0,len(list)):
            if list[i] in matching_list:
               return i+1
            matching_list.append(list[i])
        # Above for loop possibly was taking more time to execute for bigger inputs. I got time error while executing that in GEEKSforGEEKS platform
        # Hence, the above code was replaced with the following and it worked. 
        # However, see that it will work only if our list goes in a sequence as I am only maching the first element.
        # Code replacement for - LOC : 17-21
        for i in range(1,len(list)):
             if list[0] == list[i]:
               return i+1

#{
#  Driver Code Starts

if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.find(N))
# } Driver Code Ends
