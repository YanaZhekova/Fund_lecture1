budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = price_flour + price_flour * 0.25

count_bread = 0
colored_eggs = 0


price_bread = price_eggs + price_flour + (price_milk / 4)

while budget > 0:
    if budget < price_bread:
        break
    count_bread += 1
    colored_eggs += 3

    if count_bread % 3 == 0 and count_bread != 0:
        lost_eggs = count_bread - 2
        colored_eggs -= lost_eggs
    budget -= price_bread

print(f"You made {count_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")