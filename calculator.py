    def divide(a, b):
    """Divides two numbers. Raises ZeroDivisionError if b is 0. """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_user(users, id):
   def get_user(users, id):
    # Consider using .get() with a default value or explicit check
    if id not in users:
        raise KeyError(f"User with id {id} not found")
    return users[id]
   def process(items):
    result = []
    for i, item in enumerate(items):
        # Assuming the intention was to multiply by index, if not, adjust logic
        result.append(item * i)
    return result