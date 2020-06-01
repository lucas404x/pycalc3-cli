from functions.parser_functions import *
from functions.ui import *
import sys

def main():
    argc = len(sys.argv)
    values = sys.argv[1:]
    commands = ('add', 'sub', 'mult', 'div')
    subcommands = get_subcommands(values, ('-even', '-odd', '-f'), 2)
    
    if subcommands == -1 or ('-even' in subcommands and '-odd' in subcommands):
        print("Expression is wrong.")
        print("Usage: python main.py [-h or --help]")
        sys.exit(1)
    
    start = len(subcommands)
    if ('--help' in values or '-h' in values) and argc == 2:
        show_doc()
        sys.exit(0)
    
    elif argc == 1:
        print("Usage: python main.py [-h or --help]")
        sys.exit(2)

    elif not (check_commands(values[start:], commands)) or not (check_expr(values[start:])):
        print("Expression is wrong.")
        print("Usage: python main.py [-h or --help]")
        sys.exit(3)

    sys.exit(0)

if __name__ == "__main__":
    main()
