#Write a Python function to rotate/reverse a list.
def reverse_list(lst):
  """Reverses a list using slicing.

  Args:
    lst: The list to be reversed.

  Returns:
    A new reversed list.
 # """
  return lst[::-1]


def rotate_list(lst, k):
  """Rotates a list to the right by k positions.

  Args:
    lst: The list to be rotated.
    k: The number of positions to rotate by.

  Returns:
    A new rotated list.
  """
  n = len(lst)
  k = k % n  # Handle cases where k is larger than list length
  return lst[-k:] + lst[:-k]