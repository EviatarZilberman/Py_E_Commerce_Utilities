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
