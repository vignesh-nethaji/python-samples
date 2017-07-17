# Built-in Functions with Dictionary
# Function	Description
# all()	Return True if all keys of the dictionary are true (or if the dictionary is empty).
# any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
# len()	Return the length (the number of items) in the dictionary.
# cmp()	Compares items of two dictionaries.
# sorted()	Return a new sorted list of keys in the dictionary.

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: 5
print(len(squares))

# Output: [1, 3, 5, 7, 9]
print(sorted(squares))