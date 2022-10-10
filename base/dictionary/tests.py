thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"], thisdict["model"], thisdict["year"])

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
    "stuff": {
        "a": 1,
        "b": 2,
        "c": 3
    }
}

print(thisdict["stuff"]["a"])