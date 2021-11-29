def largest(arr, n):
    
    #Easier version  taken from 'geeksforgeeks'
    max = arr[0]

    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
       if arr[i] > max:
            max = arr[i]
    return max

    # Difficult version
    # My advice is to go with the easier one. The following code is a bit intimidating
    
    if len(arr) == 1:
        return arr[0];
    if len(arr) == 2:
        if arr[0] >= arr[1]:
            result = arr[0];
            return result;
        else:
            result = arr[1];
            return result;
    if len(arr) > 2:
        for i in range(len(arr)):
            if len(arr) == 2:
                break;
            if i == 0:
                for j in range(i + 1, len(arr)):
                    if arr[i] >= arr[j]:
                        result = arr[i];
                        break;
                    else:
                        arr.remove(arr[i]);
                        newArr = arr;
                        return largest(newArr, len(newArr));
                        print("new", arr);
                        break;
            else:
                for k in range(0, len(arr)):
                    if arr[k] >= arr[i]:
                        arr.remove(arr[i]);
                        newArr = arr;
                        newArr1 = newArr;
                        return largest(newArr, len(newArr));
                        print("new", arr);
                        break;
def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(largest(a, n))

        T -= 1


if __name__ == "__main__":
    main()
