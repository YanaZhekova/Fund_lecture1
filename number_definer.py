number = float(input())

if number == 0:
    print("zero")
elif 0 < number < 1000000:
    if number < 1:
        print("small positive")
    else:
        print("positive")
elif 0 > number > -1000000:
    if number > -1:
        print("small negative")
    else:
        print("negative")
elif number > 1000000:
    print("large positive")
elif number < -1000000:
    print("large negative")
