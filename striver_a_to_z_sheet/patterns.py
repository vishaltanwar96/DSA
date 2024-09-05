def pattern1(n: int) -> None:
    for row in range(n):
        for column in range(n):
            print("*", end=" ")
        print()
