n = int(input())
isOdd = False
for i in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        isOdd = True
        break

if not isOdd:
    print("All numbers are even.")