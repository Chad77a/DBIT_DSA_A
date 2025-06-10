#Count character frequencies in a string "data structures and algorithms" using a dictionary.

def count_frequencies(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Example
result = count_frequencies("data structures and algorithms")
 