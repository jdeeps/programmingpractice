# Dec 2,2021
# Problem statement :
# { You are given an array arr[], you have to re-construct an array arr[].
# The values in arr[] are obtained by doing OR(bitwise or) of consecutive elements in the array.}

def game_with_number (arr,  n) :
    newarr = []
    for i in range(0,len(arr)):
        if i == len(arr) -1:
            newarr.append(arr[i])
        else:
            newarr.append(arr[i].__or__(arr[i + 1]))
    return newarr

#{
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends
