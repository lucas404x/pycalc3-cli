from functions.parser_functions import check_commands, check_expr, get_flags
from functions.calc_functions import calc_expr
from functions.ui import show_doc
import sys

FLAGS_QUANTITY_ALLOWED = 1

def main():
    argc = len(sys.argv)
    values = sys.argv[1:]
    commands = ('add', 'sub', 'mult', 'div')
    flag = get_flags(values, ('-even', '-odd', '-f'), FLAGS_QUANTITY_ALLOWED)[0]
    flag_index = FLAGS_QUANTITY_ALLOWED if flag != None else 0

    if flag == -1:
        print("Expression is wrong.")
        print("Usage: python main.py [-h or --help]")
        sys.exit(1)

    if ('--help' in values or '-h' in values) and argc == 2:
        show_doc()
        sys.exit(0)
    
    elif argc == 1:
        print("Usage: python main.py [-h or --help]")
        sys.exit(2)

    elif not (check_commands(values[flag_index:], commands)) or not (check_expr(values[flag_index:], flag)):
        print("Expression is wrong.")
        print("Usage: python main.py [-h or --help]")
        sys.exit(3)

    result = calc_expr(values[flag_index:]) 
    result = int(result) if flag != '-f' else result
    print(result)
    
    sys.exit(0)

if __name__ == "__main__":
    main()
