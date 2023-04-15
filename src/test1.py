year = 100

for year in [1900, 1901, 2000, 2004]:
    if year % 4 != 0:
        print(f"{year}年は平年")
    elif (
        year % 100 != 0
        or year % 400 == 0
    ):
        print(f"{year}年は閏年")
    else:
        print(f"{year}年は平年")

print(year)
