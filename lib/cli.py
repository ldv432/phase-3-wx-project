from helpers import Helper

#should never crash, only goes out of program if EXPLICITELY done by user

class Cli(Helper):
        
        def main(self):
                print()
                Helper.welcome()
                while True:
                        Helper.menu()
                        user_choice = input("Type your input here: ")
                        if user_choice == ('1'):
                                Helper.list_cities()
                        #Do we want the "original" menu, or the new and improved menu
                        


if __name__ == "__main__":
        cli = Cli()
        cli.main()