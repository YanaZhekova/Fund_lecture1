budget = int(input())

command = input()

while command != "End":
    price = int(command)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
if budget >=0:
    print("You bought everything needed.")