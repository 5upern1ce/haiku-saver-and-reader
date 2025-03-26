import os, subprocess
import writinghaiku as wh
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
if os.path.exists("haikus/Otters are cute.txt") != True:
    op = open("haikus/Otters are cute.txt", "x")
    op.write("Title:Otters are cute\n\nOtters are so cute\nI love otters so much man\nThey are so cute too!")


def show_all_files():
    res = []
    length_of_list = 0
    
    for file in os.listdir(r"haikus/"):

        if file.endswith(".txt"):
            res.append(file)
            print(file)
            length_of_list += 1
    while True:
        choice = input(f"\nMake a choice (1-{length_of_list})\n")
        if choice > length_of_list or choice < 1:
            print("Invalid choice")
        else:  
            try:
                choice = int(choice)
                return res[choice - 1]
            except:
                print("Your choice was invalid!")




def create_file(file_name):
    try:
        ap = open("haikus/"+file_name+".txt", "x")
        print(Fore.GREEN +"Starting writing...")


    except:
        while flag == True:
            choice = print(Fore.RED+ Back.WHITE+"This file already exists! Would you like to overwrite it? (y/n)")
            if choice.lower() == "y":
                print(Fore.YELLOW+"Removing old file and overwriting!")
                try:
                    os.remove("haikus/"+file_name+".txt")
                    print(Fore.GREEN + "File removed!")
                    print("Please restart the program! \n")
                    program_done()
                except:
                    ("An unexpected error occured...? \nStopping the program now!")
                    flag = True
            elif choice.lower() == "n":
                print("Keeping old file!")
                flag = False
            else:
                print("Your choice was not valid! \n \n")
        program_done()
    finalhaiku = wh.writehaiku(file_name)
    ap.write(finalhaiku)
    print("The file has been saved and the haiku engraved!")
    print(finalhaiku+"\n")
    program_done()


def read_file():
    file_name = show_all_files()
    file_name = ("haikus/"+file_name)
    if os.path.exists(file_name) != True:
        print(Fore.RED + "This file does not exist!")
        program_done()
    else:
        try:
            open(file_name, "r")
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