# Merge Multiple Dictionaries

## Problem Description:

Design a Python function named `merge_three_dictionaries` to merge exactly three dictionaries into one.

### Parameters:

* `dict1` (Dictionary): The first dictionary to be merged.
* `dict2` (Dictionary): The second dictionary to be merged.
* `dict3` (Dictionary): The third dictionary to be merged.

### Returns:

* A single dictionary containing all key-value pairs from the three input dictionaries.

### Example:

```
Input: ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
```
```
Input: ({'x': 10, 'y': 20}, {'z': 30}, {'a': 40, 'b': 50})
Output: {'x': 10, 'y': 20, 'z': 30, 'a': 40, 'b': 50}
```

## Solution:

The solution is implemented [here](./code.py).
