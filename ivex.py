import os # <-- main library

def ls_func(directory = os.getcwd(), file_type = None, file_name: str = None):
        
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist")
        return  
      
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory")
        return
    
    print("="*100)
    
    for obj in os.listdir(directory):
        if file_type == None and file_name == None:
            print (f"{obj}")

        elif file_type != None and file_name == None:
            extension = ("." + str(file_type))
            if obj[-len(extension):] == extension:
                print (obj)
                
        elif file_type == None and file_name != None:        
            if file_name.lower() in obj.lower():
                print (obj)
        
        elif file_type != None and file_name != None:
            extension = ("." + str(file_type))
            if obj[-len(extension):] == extension:
                if obj[:-len(extension)].lower() == file_name.lower():
                    print (obj)
        else:
            return
                    
    print("="*100)

def indepth_ls_func(directory = os.getcwd(), file_type = None, file_name: str = None):

    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist")
        return  

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory")
        return
    
    print("="*100)
    
    for (root, dir, file) in os.walk(str(directory)):
        if file_type == None and file_name == None:
            print (f" file: {file} \n   - directory: {root}.")

        elif file_type != None and file_name == None:
            extension = ("." + str(file_type))
            for files in file:
                if files[-len(extension):] != extension:
                    pass
                else:
                    print (f" file: {files} \n  - directory: {root}.")
                    
        elif file_type == None and file_name != None:        
            for files in file:
                if file_name.lower() in files:
                    print (f" file: {files} \n  - directory: {root}.")
                    
        elif file_type != None and file_name != None:
            extension = ("." + str(file_type))  
            for files in file:
                
                if files[-len(extension):] != extension or files[:-len(extension)] != file_name.lower():
                    pass
                else:
                    print (f" file: {files} \n    - directory: {root}.")

        else:
            return

    print("="*100)

def remove_file(directory = None):
    if directory == None:
        print ("Corrext Syntax: ivex -rm [File_path]")
        return
    
    if not os.path.exists(directory):
        print(f"Error: File '{directory}' does not exist")
        return  
    
    if os.path.isdir(directory):
        print(f"Error: The path: '{directory}' is a Directory. Use the command -rmdir [DIR] to remove Directories")
        return  
    
    try:
        os.remove(directory)
    except Exception as e:
        print (f"There was an error: {e}")
    
def remove_directory(directory = None):
    if directory == None:
        print ("Corrext Syntax: ivex -rmdir [File_path].")
        return
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return  
    
    if not os.path.isdir(directory):
        print(f"Error: The path: '{directory}' does not corrispond to a Directory.")
        return  
    
    try:
        os.removedirs(directory)
    except Exception as e:
        print (f"There was a Problem: {e}")
    
def concatenate_function(file = None, max_char: int = 10000000, admin = None):
    if file == None:
        print ("Corrext Syntax: ivex -cat [File_path].")
        return

    if not os.path.exists(file):
        print(f"Error: Directory '{file}' does not exist.")
        return  

    if os.path.isdir(file):
        print(f"Error: The path: '{file}' does corrispond to a Directory. cat oly takes files as attributes.")
        return  

    try:
        if max_char == None:
            max_characters = 10000000
        else:
            max_characters = max_char

        with open(file, "r") as f:
            file_content = f.read()
        file_size = os.path.getsize(file)
        
        if admin == True:
            print (f"{file_size} Bytes")
            
        if int(file_size) >= 100000:
            yes_or_no = input("This file contains more than 100000 Characters are you sure to open it in the terminal? Y/n: ")     

            if yes_or_no.lower() != "y":
                print ("The file has been closed.")
                return
            else:
                print (file_content)
        else:
            print (file_content)   
                   
        if int(file_size) >= int(max_characters):
            
            print (f"The limit of {max_characters} has been reached. as a total of {file_size} characters have been readed.")
            countinue = input("Do you want to continue? Y/n: ")
            
            if countinue.lower() != "y":
                print ("The file has been closed.")
                return
            
    except Exception as e:
        print (f"There was an Unexpected Error: {e}")

def who_am_i():
    print (os.getlogin())

def touch_func(file_name):
    if os.path.exists(file_name):
        print(f"Error: File '{file_name}' already exist")
        return  
    
    try:
        with open(os.path.join(os.getcwd(), file_name), "w") as fp:
            pass
    except Exception as e:
        print(f"There was an Unexpected error: {e}")
   
def make_directory(dir_name: str):
    
    if os.path.exists(dir_name):
        print(f"Error: Directory '{dir_name}' already exist")
        return  
    
    try:
        os.mkdir(dir_name)
    except Exception as e:
        print (f"there was an unexpected error: {e}")
        
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