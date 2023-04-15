# -*- coding: utf-8 -*-

def main():
    for year in [1900, 1901, 2000, 2004]:
        print(f"{year}の判定")

        if year % 4 != 0:
            print(normal_year(year))
        elif (
            year % 100 != 0
            or year % 400 == 0
        ):
            print(leap_year(year))
        else:
            print(normal_year(year))


def leap_year(year: int) -> str:
    return f"{year}は閏年"


def normal_year(year: int) -> str:
    return f"{year}は平年"


if __name__ == "__main__":
    main()
