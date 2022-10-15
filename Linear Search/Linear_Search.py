# define search function 
def search(arr, N, x):
    #iterate through array until match is found equal to userInput
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1 
 
# Driver Code
if __name__ == "__main__":
    # the array to iterate and return results from
    arr = [2, 4, 7, 10, 11 ,32 ,45, 87]
    print(arr)
    # userInput to determine where in array a value is located
    userInput = int(input("Enter a value: "))
    x = userInput
    N = len(arr)
    output = "  was not found."
    outputResult = str(userInput) + str(output) 
 
    # Function call to print results of where in an array the value is located
    result = search(arr, N, x)
    if(result == -1):
        print(outputResult)
    else:
        print("Found", x, "at index", result, "using Python")