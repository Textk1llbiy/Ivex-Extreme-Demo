import os

def make_directory(dir_name: str):
    
    if os.path.exists(dir_name):
        print(f"Error: Directory '{dir_name}' already exist")
        return  
    
    try:
        os.mkdir(dir_name)
    except Exception as e:
        print (f"there was an unexpected error: {e}")