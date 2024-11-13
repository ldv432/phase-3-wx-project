from helpers import Helper

#should never crash, only goes out of program if EXPLICITELY done by user

class Cli(Helper):
        
        def main(self):
                Helper.welcome()
                while True:
                        Helper.menu()
                        user_choice = input("> ")
                        if user_choice == ('1'):
                                Helper.list_cities()
                        


if __name__ == "__main__":
        cli = Cli()
        cli.main()