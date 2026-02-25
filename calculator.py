def divide(a, b):
    # BUG: no check for division by zero
    return a / b

def get_user(users, id):
    # BUG: no bounds check, will throw KeyError
    return users[id]

def process(items):
    result = []
    for i in range(len(items)):
        # BUG: off-by-one, should be i+1 or enumerate
        result.append(items[i] * i)
    return result
