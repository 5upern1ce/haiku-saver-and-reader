import filehandling as fh

def main():
    flag = True
    while flag == True:
        choice = input("Make a choice of:\n1.Create a Haiku \n2.Open and read a Haiku \n3.Close program\n")
        try:
            choice =int(choice)
            if choice != 1 and choice != 2 and choice != 3:
                print("Invalid Choice!")
            else:
                if choice == 1:
                    file_name=input("What is the title of your poem?")
                    fh.create_file(file_name)
                if choice == 2:
                    fh.read_file()
                else:
                    fh.program_done()
        except:
            print("Invalid Choice!")


main()