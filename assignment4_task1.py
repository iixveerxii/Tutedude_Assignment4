# Read a File and Handle Errors

#  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

'''to create 'sample.txt'''
# with open("sample.txt", "wt") as fh:
#     fh.write("This is a sample text file. \n")
#     fh.write("It contains multiple lines")

try:
    with open("sample.txt", "rt") as fh:
        data = fh.readlines()

        print("reading file content:")

        for line in range(len(data)):
            print(f"line {line+1}: {data[line].rstrip("\n")}")

except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found")


