def pattern1(n: int) -> None:
    for row in range(n):
        for column in range(n):
            print("*", end=" ")
        print()


def pattern2(n: int) -> None:
    for row in range(1, n+1):
        for column in range(row):
            print("*", end=" ")
        for column in range(n - row):
            print(" ", end=" ")
        print()


def pattern3(n: int) -> None:
    for row in range(1, n+1):
        for column in range(1, row+1):
            print(str(column), end=" ")
        for column in range(n - row):
            print(" ", end=" ")
        print()


def pattern4(n: int) -> None:
    for row in range(1, n+1):
        for column in range(row):
            print(row, end=" ")
        for column in range(n - row):
            print(" ", end=" ")
        print()
