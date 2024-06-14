command = input()
new_text = ""

while command != "End":
    if command != "SoftUni":
        for char in command:
            new_text += char
            new_text += char
        print(new_text)
    new_text = ""
    command = input()
