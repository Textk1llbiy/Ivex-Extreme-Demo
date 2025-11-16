import os

def touch_func(file_name):
    if os.path.exists(file_name):
        print(f"Error: File '{file_name}' already exist")
        return  
    
    try:
        with open(os.path.join(os.getcwd(), file_name), "w") as fp:
            pass
    except Exception as e:
        print(f"There was an Unexpected error: {e}")