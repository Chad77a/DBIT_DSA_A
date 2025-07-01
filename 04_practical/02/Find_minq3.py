def find_min(lst):
    if not lst:
        return None
    min_value = lst[0]
    for element in lst:
        if element < min_value:
            min_value = element
    return min_value

# Example usage:
print(find_min([1, 2, 3, 4])) 