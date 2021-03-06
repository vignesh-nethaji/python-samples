# Python Dictionary Methods
# Method	Description
# clear()	Remove all items form the dictionary.
# copy()	Return a shallow copy of the dictionary.
# fromkeys(seq[, v])	Return a new dictionary with keys from seq and value equal to v (defaults to None).
# get(key[,d])	Return the value of key. If key doesnot exit, return d (defaults to None).
# items()	Return a new view of the dictionary's items (key, value).
# keys()	Return a new view of the dictionary's keys.
# pop(key[,d])	Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
# popitem()	Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
# setdefault(key[,d])	If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
# update([other])	Update the dictionary with the key/value pairs from other, overwriting existing keys.
# values()	Return a new view of the dictionary's values

marks = {}.fromkeys(['Math','English','Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))