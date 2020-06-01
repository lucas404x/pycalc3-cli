from functions.parser_functions import *
import sys

def main():
    argc = len(sys.argv)
    values = sys.argv[1:]
    commands = ('add', 'sub', 'mult', 'div', '-f')
    
    if ('--help' in values or '-h' in values) and argc == 2:
        print("This is PyCalc!")
        print("Available commands:")
        print("add - sum two values; x [add] y")
        print("sub - subtract two values; x [sub] y")
        print("multi - multiply two values; x [multi] y")
        print("div - divide two values; x [div] y")
        print("\nUse the '-f' flag to float numbers.")
        print("\nExample: 10 add 60 div 2 add 2")
        print("42")
        sys.exit(0)
    
    elif argc == 1:
        print("Usage: python main.py [-h or --help]")
        sys.exit(1)

    elif not (check_commands(values, commands)) or not (check_expr(values)):
        print("Expression is wrong.")
        print("Usage: python main.py [-h or --help]")
        sys.exit(2)

    sys.exit(0)

if __name__ == "__main__":
    main()
