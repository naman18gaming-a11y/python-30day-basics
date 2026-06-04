# Count total lines in a file
with open("data.txt", "r") as file:
    content = file.read()
lines =  content.splitlines()
print("Total lines in the file:", len(lines))
