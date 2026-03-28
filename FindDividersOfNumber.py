# --coding:utf-8--

import os

os.system("cls")
print("Input an integer positive number")
ulNumber = int(input())
print(f"The number {ulNumber} has the folowing divisors:")
for i in range(1, ulNumber + 1):
    if ulNumber % i == 0:
        print(i, end=" ")
print
