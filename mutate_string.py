text1 = input()
text2 = input()

last_text = ""
for i in range(len(text1)):
    new_text = ""
    for j in range(0, i + 1):
        char = text2[j]
        new_text += char
    for n in range(i + 1, len(text1)):
        char = text1[n]
        new_text += char
    if i == 0:
        last_text = new_text
        print(new_text)
    else:
        if last_text != new_text:
            last_text = new_text
            print(new_text)

