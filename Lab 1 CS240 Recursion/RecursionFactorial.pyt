# Define a function called 'faktorial' that takes one argument 'n'
def faktorial(n):
    # Check if 'n' is 0 or 1, which is the base case for the factorial function
    if n == 0 or n == 1:  
        # If 'n' is 0 or 1, return 1, since the factorial of 0 and 1 is defined as 1
        return 1
    # If 'n' is not 0 or 1, call the 'faktorial' function again with 'n-1' and multiply the result by 'n'
    # This is the recursive case, where the function breaks down the problem into smaller sub-problems
    return n * faktorial(n - 1)  

# Call the 'faktorial' function with the argument 5 and print the result
print(faktorial(5))  # Output: 120
