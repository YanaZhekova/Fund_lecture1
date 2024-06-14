import math

buy_quantity_decorations = int(input())
days_left_to_christmas = int(input())

days = 0
sum = 0.0
spirit_points = 0
while days_left_to_christmas > 0:

    days += 1
    if days % 2 == 0:
        sum += buy_quantity_decorations * 2
        spirit_points += 5
    if days % 3 == 0 and days % 5 != 0:
        sum += buy_quantity_decorations * 3
        sum += buy_quantity_decorations * 5
        spirit_points += 10
        spirit_points += 3
    if days % 5 == 0 and days % 3 != 0:
        sum += buy_quantity_decorations * 15
        spirit_points += 17
    if days % 5 == 0 and days % 3 == 0:
        sum += buy_quantity_decorations * 15
        sum += buy_quantity_decorations * 3
        sum += buy_quantity_decorations * 5
        spirit_points += 30

    if days % 10 == 0:
        spirit_points -= 20
        sum += 1 * 5
        sum += 1 * 3
        sum += 1 * 15

    if days % 11 == 0:
        buy_quantity_decorations += 2

    if days_left_to_christmas == 1 and days == 10:
        spirit_points -= 30

    days_left_to_christmas -= 1

print(f"Total cost: {math.floor(sum)}")
print(f"Total spirit: {spirit_points}")
