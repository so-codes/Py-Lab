# create a file wich contains 10 lines of text. Determine weather a search stream is present in the file or not.

def search_stream(file_name):
    with open(file_name, "r") as f:

        print("Enter the search stream: ")
        stream = input()

        for line in f:
            if stream in line:
                print(stream, "is present in the file" + " with line : ", line)
                return True
    print(stream, "is not present in the file")
    return False

search_stream("/home/criz/Documents/GitHub/py-up/tst/oi.txt")