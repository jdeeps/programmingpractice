# Date - Nov 29,2021 - This is a programming question under  Algorithm section of GeeksforGeeks
# Problem statement -
# { You are given an array arr[], you have to re-construct an array arr[].
# The values in arr[] are obtained by doing Xor of consecutive elements in the array. }

def game_with_number(arr, n):
    newarr = []
    for i in range(0, len(arr)):
        if i == len(arr) - 1:
            newarr.append(arr[i])
        else:
            res = arr[i].__xor__(arr[i + 1])
            newarr.append(res)

    return newarr


def get_result():
# {
#  Driver Code Starts
# Initial Template for Python 3

    for _ in range(0, int(input())):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = game_with_number(arr, n);
        print(*res)

# } Driver Code Ends

if __name__ == "__main__":
    get_result()

#Notes - Want to know why that print(*res) is used - https://stackoverflow.com/questions/61562134/in-print-function-in-python
