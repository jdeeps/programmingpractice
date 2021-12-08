# --------------------------------------------------------------------------------
# Date Dec 8,2021
# Problem statement :
# { Given an array, rotate the array by one position in clock-wise direction.}
# --------------------------------------------------------------------------------

def rotate(arr, n):
    rotate_arr =[]
    # Adding the last element to the newly created temporary array
    rotate_arr.append(arr[-1])
    # Now,adding rest of the elements except the last one
    for i in range(len(arr)-1):
        rotate_arr.append(arr[i])
    # Reassigning adding the values from newly created temporary array to the existing array and returning the same
    arr = rotate_arr
    return arr

# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        # Modified below code to reassign the returned value from function to array 'a' and then print
        # This can not be done in GeeksForGeeks platform as the driver code is not editable
        a = rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
