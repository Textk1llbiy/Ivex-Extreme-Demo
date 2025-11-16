import os

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