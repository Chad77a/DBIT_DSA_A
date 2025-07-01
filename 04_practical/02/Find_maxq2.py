def find_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for element in lst:
        if element > max_value:
            max_value = element
    return max_value

# Example usage:
print(find_max([1, 2, 3, 4]))  