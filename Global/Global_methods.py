def convert_enum(ins):
    if ins is None:
        return None

    if '_' not in ins:
        return ins

    result = ''
    for char in ins:
        if char != '_':
            result += char
        else:
            result += ' '

    return result


def is_type_of(arg, item_type):
    return isinstance(arg, item_type)


def compare_lists(list_a, list_b) -> bool:
    if list_a is None or list_b is None:
        return False

    for item_a in list_a:
        for item_b in list_b:
            if item_a.lower() == item_b.lower():
                return True

    return False
