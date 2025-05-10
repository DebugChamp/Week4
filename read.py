with open("input.txt", "r") as file:
    content = file.read()

modified_content = content.upper()

with open("output.txt", "w") as file:
    file.write(modified_content)
