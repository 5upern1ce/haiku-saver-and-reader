import os, subprocess, writinghaiku
try:
    import time
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
except:
    print("Updating the required modules: colorama, time, os!")
    try:
        subprocess.run(["python", "-m", "pip", "install", "time"])
        subprocess.run(["python", "-m", "pip", "install", "os"])
        subprocess.run(["python", "-m", "pip", "install", "colorama"])
        print("Modules updated successfully\n")
        os._exit(0)
    except:
        print("Failed to update the required modules\n")
        os._exit(0)
    

flag = True

if os.path.exists("haikus") != True:
    os.makedirs("haikus")

def create_file(file_name):
    try:
        open(file_name+".txt", "x")
        print(Fore.GREEN +"Starting writing...")


    except:
        while flag == True:
            choice = print(Fore.RED+ Back.WHITE+"This file already exists! Would you like to overwrite it? (y/n)")
            if choice.lower() == "y":
                print(Fore.YELLOW+"Removing old file and overwriting!")
                try:
                    os.remove(file_name+".txt")
                    print(Fore.GREEN + "File removed!")
                except:
                    ("An unexpected error occured...? \nStopping the program now!")
                    flag = True
            elif choice.lower() == "n":
                print("Keeping old file!")
                flag = False
            else:
                print("Your choice was not valid! \n \n")
        program_done()

def append_file(file_name):
    if os.path.exists(file_name+".txt") != True:
        print(Fore.RED + "This file does not exist!")
        program_done()
    else:
        try:
            open(file_name+".txt", "a")
            print(Fore.GREEN +"File opened successfully!")
        except:
            print(Fore.RED + "An unexpected error occured...? \nStopping the program now!")
            program_done()
    


def program_done():
    print("Exiting program\n")
    time.sleep(1)
    print(Fore.GREEN + "3\n")
    time.sleep(1)
    print(Fore.YELLOW + "2\n")
    time.sleep(1)
    print(Fore.RED + "1\n")
    time.sleep(1)
    print(Fore.LIGHTCYAN_EX + "Goodbye!")