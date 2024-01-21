import argparse
from .todo import ToDo


def main():
    #defining the parser
    parser = argparse.ArgumentParser(prog = "TODO List application", description="to-do list")
    parser.set_defaults(func=lambda _: parser.print_help())
    parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 0.1.0')
    subparsers = parser.add_subparsers(title = 'subcommands', dest='command')
    list_parser = subparsers.add_parser("list", help = 'This command gets the list of todos')
    #parser.add_argument('command', choices=['list'], help='This command gets the list of todos')
    list_parser.add_argument('--value', type=int, default=40, help='Value for the list command')
    list_parser.add_argument('--pending', action='store_true', help='Show pending todos')
    args = parser.parse_args()

    #Creating an object
    myApp = ToDo()
    if args.command == 'list':
        myApp.listToDo(args.value, args.pending)
if __name__ == "__main__":
    main()
