#! /usr/bin/env python3
x, y, z = map(int, input().split())
product = x * y * z
if product > 0:
    print("Positive")
elif product == 0:
    print("Negative or positive?")
else:
    print("Negative")
