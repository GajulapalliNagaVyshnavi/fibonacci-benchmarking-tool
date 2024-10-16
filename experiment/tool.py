def fibonacci_tool(n):
    """
    A simple tool that calculates the nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# you can create a more complex function to visualize the different methods in different complexities 
