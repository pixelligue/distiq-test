from typing import Any
from typing import Any

def divide(a: int | float, b: int | float) -> float:
    """Делит число a на число b.

    Возбуждает ZeroDivisionError, если b равно нулю.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
    return users.get(user_id)

def process(items: list[int | float]) -> list[int | float]:
    result = []
    for i, item in enumerate(items):
        result.append(item * i)
    return result