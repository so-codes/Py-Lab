# Write a Python script to sort (ascending and descending) a dictionary by value.

def ascending(n):
    print("Ascending:")
    for key, value in sorted(n.items()):
        print(key, value)


def descending(n):
    print("Descending:")
    for key, value in sorted(n.items(), reverse=True):
        print(key, value)

ascending({'a': 1, 'b': 2, 'c': 3})
descending({'a': 1, 'b': 2, 'c': 3})