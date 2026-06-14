from pathlib import Path
import os


def create_file():
    try:
        name = input("enter file name :")
        path = Path(name)
        if not path.exists():
            with open(path, "w") as file:
                content = input("what you want to write in this file :")
                file.write(content)
            print("file create successfully")
        else:
            print("file already exist")
    except Exception as file:
        print(f"an error occured {file}")


def read_file():
    try:
        name = input("enter file name :")
        path = Path(name)
        if path.exists():
            with open(path, "r") as file:
                print(file.read())
        else:
            print("file not exist")
    except Exception as err:
        print(f"error occured {err}")


def update_file():
    choose = int(input(
        '''
     1.rename
     2. content add
     3. over writting
     '''
    ))
    if choose == 1:
        try:
            new_file = input("enter name of new file:")  # input new file name
            new_path = Path(new_file)  # new path object
            if not new_path.exists():  # check new file exist or not
                old_file = input("enter your old file:")  # input old file
                old_path = Path(old_file)  # create object of old file
                if old_path.exists():
                   old_path.rename(new_file)
                   print("file name changed successfully")
                else:
                    print("file not exist")
            else:
                print("file already exist")
        except Exception as err:
            print(f"err occured {err}")
    if choose == 2: 
        try:
            name = input("enter file name:")
            path1 = Path(name)
            if path1.exists():
                with open(path1, "a") as file:
                    data = input("enter data what you want to add:")
                    file.write(" \n" + data)
            else:
                    print("file not exist")
        except Exception as err:
            print(f"error occured {err}")
    if choose == 3:
        try:
            file_name = input("enter file name:")
            path = Path(file_name)
            if path.exists():
                with open(path, "w") as file:
                    data = input("Enter what you want to overwrite")
                    file.write(data)
            else:
                    print("file not exist")
        except Exception as err:
           print(f"error occured {err}")

def delete_file():
    try:

        file_name = input("enter file name")
        path = Path(file_name)
        if path.exists():
            path.unlink()
        print("file deleted successfull")
    except Exception as err:
        print(f"error {err}")        


print("Hey! what you want to do today ")
print("please choose 1 to create  file :")
print("please choose 2 to read the file :")
print("please choose 3  to update the file :")
print("please choose 4  to delete the file :")
choice = int(input("enter number for further process:"))


if choice == 1:
    create_file()
elif choice == 2:
    read_file()
elif choice == 3:
    update_file()
elif choice == 4:
    delete_file()
