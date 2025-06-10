#A function using tail recursion that sums all numbers up to n.

def sum_up_to(n, total=0):
    if n == 0:
        return total
    return sum_up_to(n - 1, total + n)  # Recursive call