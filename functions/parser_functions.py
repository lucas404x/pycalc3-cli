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

def get_subcommands(values, subcommands, max_subcommands):
    subcommands_ = []

    # make sure it appears only once
    for subcommand in subcommands:
        if values.count(subcommand) > 1:
            return -1
        elif values.count(subcommand) == 1:
            subcommands_.append(subcommand)
            
    if len(subcommands_) > max_subcommands:
        return -1
    
    return subcommands_