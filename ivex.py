import os # <-- main library

#Practically meme
def who_am_i():
    print (os.getlogin())
        
def echo_func(what_to_print: str):
    print (what_to_print)   
      
def create_parser():
    import argparse # <- cli library
    
    # 1. Create the parser object
    parser = argparse.ArgumentParser(
        prog="ivex",
        description="This will make you able to use linux syntax [Extreme-BETA]",
        usage="%(prog)s [specific command]",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # 2. Add arguments
    parser.add_argument("--admin",
                        action="store_true",
                        help = "Gives specific logs for Debugging reasons.")
    
    parser.add_argument("-ls", "--list", 
                        nargs = '?', 
                        const = os.getcwd(),
                        metavar = "DIR",
                        help = "This will give you a list of all the files present in the current directory.")
    
    parser.add_argument("-idls", "--indepthlist", 
                        nargs = '?', 
                        const = os.getcwd(),
                        metavar = "DIR",
                        help = "Gives all the files present in the current directory and also the sub-directories [adding dir position to every file].")
    
    parser.add_argument("-ft", "--file_type",
                        nargs = '?', 
                        const = None,
                        metavar = "DIR",
                        help = "This is to add to the -idls -ls (--indepthlist, --list) as the file format only without anything else. [it has no default value]")
    
    parser.add_argument("--name",                        
                        nargs = '?', 
                        const = None,
                        metavar = "DIR",
                        help = "This is to add to the -idls, -ls (--indepthlist, --list) as the name of the file you are searching. [it has no default value]")
    
    parser.add_argument("-rm", "--remove",
                        nargs = '?',
                        const = None,
                        metavar = "FileDIR",
                        help = "This will give you the ability to specify what file (not directory) to delete.")
    
    parser.add_argument("-rmdir", "--removedirectory",
                        nargs = '?',
                        const = None,
                        metavar = "DIR",
                        help = "Gives you the ability to specify what directory (directory) to delete.")
    
    parser.add_argument("-cat", "--concatenate",
                        nargs = '?',
                        const = None,
                        metavar = "FileDir",
                        help = "the command cat will write for you all the content of the specified file you select.")
    
    parser.add_argument("-maxchar", "--maxcharacters",
                        nargs = '?',
                        const = 10000000,
                        metavar = "Intiger",
                        help = "This command is used in cat to set a maximum amount of characters before opening it.")
    
    parser.add_argument("-whoami",
                        action = "store_true",
                        help = "this will solve the temporary identity crisis that programming has given you.")

    parser.add_argument("-touch",
                        nargs = '?',
                        const = None,
                        metavar = "File_name",
                        help = "This command will create a file on the current directory with the name and extension that you say.")
    
    parser.add_argument("-mkdir", "--makedirectory",
                        nargs = '?',
                        const = None,
                        metavar = "Dir Name",
                        help = "This will create a directory to the current working directory.")
    
    parser.add_argument("-echo",
                        nargs = '?',
                        const = None,
                        metavar = "What to echo",
                        help = "This will simply print out what you write on it.")

    # 3. Parse the arguments
    args = parser.parse_args()
    return args

def main():
    args = create_parser()
    
    from functions.list_function import ls_func
    from functions.Indepthlist_function import indepth_ls_func
    from functions.remove_file_function import remove_file
    from functions.remove_directory_function import remove_directory
    from functions.concatenate_function import concatenate_function
    from functions.touch_function import touch_func
    from functions.make_directory_function import make_directory
    
    # DEBUG ONLY FUNCTION
    if args.admin:
        print("Parsed Arguments:")
        for arg in vars(args):
            print(f"  {arg}: {getattr(args, arg)}")
    
    if args.list != None:
        ls_func(directory = args.list, file_type = args.file_type, file_name = args.name)

    elif args.indepthlist != None:
        indepth_ls_func(directory = args.indepthlist, file_type = args.file_type, file_name = args.name) 

    elif args.remove != None:
        remove_file(directory = args.remove)

    elif args.removedirectory != None:
        remove_directory(directory = args.removedirectory)       

    elif args.concatenate != None:
        concatenate_function(file = args.concatenate, max_char = args.maxcharacters, admin = args.admin)

    elif args.whoami == True:
        who_am_i()
    
    elif args.touch != None:
        touch_func(file_name = args.touch)    

    elif args.makedirectory != None:
        make_directory(dir_name = args.makedirectory)

    elif args.echo != None:
        echo_func(what_to_print = args.echo)  

if __name__ == "__main__":
    main()
    
    
    
    
    