from typing import Any
    """Делит число a на число b.

    Возбуждает ZeroDivisionError, если b равно нулю.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_user(users: dict, user_id: Any) -> Any | None:
    """Возвращает пользователя по его ID из словаря.

    Возвращает None, если пользователь не найден.
    """
    return users.get(user_id)

def process(items: list[int | float]) -> list[int | float]:
    """Обрабатывает список элементов, умножая каждый элемент на его индекс.

    Предполагается, что индексация начинается с 0.
    """
    result = []
    for i, item in enumerate(items):
        result.append(item * i)
    return result