command = input()
numbers_of_coffees = 0

while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        numbers_of_coffees += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        numbers_of_coffees += 2

    command = input()

if numbers_of_coffees > 5:
    print("You need extra sleep")
else:
    print(numbers_of_coffees)
