divisor = int(input())
boundary = int(input())
max_number =0

for i in range(boundary, 0, -1):
    if i % divisor == 0:
        if i > max_number:
            max_number = i

print(max_number)