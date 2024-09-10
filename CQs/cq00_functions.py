"""My first challenge question in COMP110!"""

__author__ = "730814121"


def mimic(message: str) -> str:
    """Function that repeats whatever you input for message back to you"""
    return message


def main() -> None:
    """Function prints the result of calling the function mimic"""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
