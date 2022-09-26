def search(arr, N, x):
 
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1

#string = int(input("Enter a valie: "))
 
 
# Driver Code
if __name__ == "__main__":
    arr = [2, 4, 7, 10, 11 ,32 ,45, 87]
    print(arr)
    userInput = int(input("Enter a value: "))
    x = userInput
    N = len(arr)
    output = "  was not found."
    outputResult = str(userInput) + str(output) 
 
    # Function call
    result = search(arr, N, x)
    if(result == -1):
        #print(x + "Element is not present in array")
        print(outputResult)
    else:
        # print("Element is present at index", result)
        print("Found", x, "at index", result)