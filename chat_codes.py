n = int(input())
for i in range(n):
    number = int(input())
    if number <= 88:
        if number == 88:
            print("Hello")
        elif number == 86:
            print("How are you?")
        else:
            print("GREAT!")
    elif number > 88 :
        print("Bye.")
