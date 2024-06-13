n = int(input())

for i in range(n):
    text = input()
    if text.__contains__(".") or text.__contains__(",") or text.__contains__("_"):
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")