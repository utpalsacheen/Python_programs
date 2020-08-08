a = [12, 45, 2, 41, 31, 10, 8, 6, 4]

first = 0
sec = 0

for num in a:
    if num > first:
        first = num
    elif sec != first and num > sec:
        sec = num

print first
print sec
