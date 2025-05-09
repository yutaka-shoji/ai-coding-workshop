# Exercise: Roo check type analysis result. Try to fix the type error
def get_numbers() -> list[int]:
    # Type check error: Returning List[str] where List[int] is expected
    # Runtime: Works fine because strings are convertible to integers
    return ["1", "2", "3"]


def main() -> None:
    numbers = get_numbers()
    total = sum(int(n) for n in numbers)  # Converts strings to integers at runtime
    print(f"Sum: {total}")


if __name__ == "__main__":
    main()
