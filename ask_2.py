class Asking:
    my_list = []

    def ask_me(self):
        self.names = input("Enter Name > ").lower()
        if len(self.names) <= 1:
            print("longer name")


        if self.names in self.my_list:
            print("Name Has Been Taken Already Try Again")

        elif self.names not in self.my_list:
            self.my_list.append(self.names)

            if len(self.my_list) == 5:
                print(self.my_list)



    # add a name checking if name in my_list print info on them
    # add age checking
    # add info page to then check info on

Asking()
