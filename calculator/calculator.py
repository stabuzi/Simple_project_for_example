from calculator.utils import helpers


class Calculator:
    def __init__(self) -> None:
        helpers.health()
        print("labas")


def sum(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    c = Calculator()
