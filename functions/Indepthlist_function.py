import os

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
    