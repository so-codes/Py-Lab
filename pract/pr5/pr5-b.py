# Write a Python script to concatenate following dictionaries to create a new one

def concat_dict(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3

print(concat_dict({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}))