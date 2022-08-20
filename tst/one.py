# create a dictionary structure to store the class and room number of programs whole lecturers are conducted on 6th foor.
# add a new program with its class name and room number to the existing structure.

clg = {
    "lecturer1": {
        "class1": "room1",
        "class2": "room2",
        "class3": "room3",
        "class4": "room4",
        "class5": "room5"
    },
    "lecturer2": {
        "class1": "room1",
        "class2": "room2",
        "class3": "room3",
        "class4": "room4",
        "class5": "room5"
    },
}

print(clg, "\n")

clg["lecturer3"] = {
    "class1": "room1",
    "class2": "room2",
    "class3": "room3",
    "class4": "room4",
    "class5": "room5"
}

print(clg)  