import argparse
from .todo import ToDo


def main():
    #defining the parser
    parser = argparse.ArgumentParser(prog = "TODO List application", description="to-do list")
    parser.set_defaults(func=lambda _: parser.print_help())
    parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 0.1.0')
    subparsers = parser.add_subparsers(title = 'subcommands', dest='command')
    list_parser = subparsers.add_parser("list", help = 'This command gets the list of todos')
    list_parser.add_argument('--number', type=int, default=20, help='The number od todos displayed')
    list_parser.add_argument('--pending', action='store_true', help='Show pending todos')
    list_parser.add_argument('--option', choices=['even', 'odd', 'all'], default='even',
                             help="Specify 'even', 'odd', or 'all' for TODO IDs")
    args = parser.parse_args()
    
    #Creating an object
    myApp = ToDo()
    if args.command == 'list':
        if args.option == 'even' or args.option == 'odd':
            args.number *= 2
        myApp.listToDo(args.number, args.pending,args.option)
if __name__ == "__main__":
    main()
