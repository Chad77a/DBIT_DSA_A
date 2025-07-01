def linear_search(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1

# Example usage:
print(linear_search([1, 2, 3, 4], 3)) 