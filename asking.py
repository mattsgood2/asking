class Asking:

    def __init__(self):
        self.my_list = []
        while True:
            self.names = input("Enter Name > ").lower()
            if len(self.names) <= 1:
                print("longer name")


            if self.names in self.my_list:
                print("Name Has Been Taken Already Try Again")

            elif self.names not in self.my_list:
                self.my_list.append(self.names)

                if len(self.my_list) == 5:
                    print(self.my_list)
                    break


#C:\Program Files\Common Files\Microsoft Shared\Windows Live;C:\Program Files (x86)\Common Files\Microsoft Shared\Windows Live;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Windows Live\Shared;C:\Program Files\nodejs\



#C:\Users\Matt\AppData\Local\Programs\Python\Python35-32\Scripts\;C:\Users\Matt\AppData\Local\Programs\Python\Python35-32\;C:\Ruby22\bin;C:\Users\Matt\AppData\Roaming\npm;C:\Users\Matt\AppData\Local\atom\bin









    # add a name checking if name in my_list print info on them
    # add age checking
    # add info page to then check info on

Asking()
