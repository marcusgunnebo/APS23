#! /usr/bin/env python3
x, y, z = map(int, input().split())
product = x * y * z
if product > 0:
    print("Negative")
elif product == 0:
    print("Positive")
else:
    print("Negative or positive?")
