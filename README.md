# Calculator CLI

**Tier:** 2-Intermediate

This is my version from Calculator CLI made in Python 3.

The challenge was from this [repository.](https://github.com/florinpop17/app-ideas)

## User Stories

- [x] User can add multiple numbers using `add` command.
- [x] User can add floating numbers using the `-f` flag.
- [x] User can add only even/odd numbers using `even`/`odd` sub-command.
- [x] User can use `--help` or `-h` flag to get all the available commands and flags.
 

## Bonus Features

- [x] User can use all the basic arithmetic operations like (addition, subtraction, multiplication and divison).
- [ ] User can use `--help` or `-h` flag to get the sub-commands of command.
- [ ] **Power of** and **Square Root of** operation.

## Example

```
python main.py -f 3.4 add 3.2 add sub 3.2
> 3.4

python main.py -odd 3 add 9 div 3
> 6
```