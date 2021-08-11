year = int(input())
youn = (year % 4 == 0) and ((year % 100 != 0) or
    year % 400 == 0)
print(1) if youn else print(0)
