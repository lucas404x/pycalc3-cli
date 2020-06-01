import re

def check_commands(values, commands):
    for value in values:
        if not (value in commands) and (not value.isdigit() and not is_float_number(value)):
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
        elif (values[i].isdigit() == values[i + 1].isdigit()) and flag != '-f':
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
    if len(re.findall(r'(\.)', string)) != 1:
        return False
    if re.search(r'(\d+\.\d+)', string) == None:
        return False
    
    aux = re.split(r"[^a-z]\d+\.\d+", string)
    for i in aux:
        if not i in (string, ''):
            return False

    return True
