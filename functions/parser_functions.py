def check_commands(values, commands):
    for value in values:
        if not (value in commands) and not (value.isdigit()):
            return False
    return True

def check_expr(values):
    if len(values) % 2 == 0:
        return False
    for i in range(len(values)):
        if i == len(values) - 1:
            continue
        elif values[i].isdigit() == values[i + 1].isdigit():
            return False
    
    return True