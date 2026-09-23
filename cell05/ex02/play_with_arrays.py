#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for value in original_array:
    if value > 5:
        new_array.append(value + 2)

print(original_array)
print(new_array)