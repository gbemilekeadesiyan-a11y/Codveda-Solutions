filename = input("Enter the filename: ")

#Read File

try:
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"The file '{filename}' contains {word_count} words.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")