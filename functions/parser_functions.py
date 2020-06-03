import re

def check_commands(values, commands):
    for value in values:
        if not (value in commands) and not (is_number(value, int) or is_float_number(value)):
            return False
    return True


def check_expr(values, flag):
    if len(values) % 2 == 0:
        return False

    for i in range(len(values)):
        is_floatA = is_float_number(values[i])
        if not values[i].isalpha() and ((is_floatA and flag != '-f') or (not is_floatA and flag == '-f')):
            return False

        if flag == '-odd' and values[i].isdigit():
            if int(values[i]) % 2 == 0:
                return False
        elif flag == '-even' and values[i].isdigit():
            if int(values[i]) % 2 != 0:
                return False

        if i == len(values) - 1:
            continue
        else:
            is_floatB = is_float_number(values[i + 1])

        if (is_floatA == is_floatB) and flag == '-f':
            return False
        elif (is_number(values[i], int) == is_number(values[i + 1], int)) and flag != '-f':
            return False

    return True


def get_flags(values, subcommands, max_subcommands):
    subcommands_ = []

    # make sure it appears only once
    for subcommand in subcommands:
        if values.count(subcommand) > 1:
            return -1
        elif values.count(subcommand) == 1:
            subcommands_.append(subcommand)

    if len(subcommands_) > max_subcommands:
        return -1

    return subcommands_ if len(subcommands_) > 0 else [None]

def is_float_number(string):
    pattern = r'\d+\.\d+'
    return True if re.split(pattern, string).count('') == 2 else False

def is_number(value, type_):
    try:
        number = type_(value)
    except ValueError:
        return False
    else:
        return True
