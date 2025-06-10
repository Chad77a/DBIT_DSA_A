#A function using head recursion that counts down from n to 0.
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)  # Recursive call