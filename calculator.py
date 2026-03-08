from typing import Any

def divide(a: int | float, b: int | float) -> float:
    """Делит число a на число b.

    Возбуждает ZeroDivisionError, если b равно нулю.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def process(items: list[int | float]) -> list[int | float]:
    """Обрабатывает список чисел, умножая каждый элемент на его индекс."""
    result = []
    for i, item in enumerate(items):
        result.append(item * i)
    return result