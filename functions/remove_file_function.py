import os

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
        