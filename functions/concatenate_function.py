import os

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