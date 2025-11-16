import os

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