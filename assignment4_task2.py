# Task 2: Write and Append Data to a File

# Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

user_input = input("enter text to write to the file: ")

with open("output.txt", "wt") as fh:
    fh.write(user_input+"\n")
print(f"data successfully written to 'output.txt'\n")

add_data = input("enter additional text to append: ")

with open("output.txt", "at") as fh:
    fh.write(add_data+"\n")
print(f"data successfully appended.\n")

with open("output.txt", "rt") as fh:
    content = fh.read()
    print(f"final content of 'output.txt':")
    print(content)



