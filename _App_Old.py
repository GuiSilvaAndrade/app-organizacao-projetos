import os  # Create and move folders
import shutil  # Move folders
from tkinter import *  # Interface


class CreatesFolder_MoveFile:
    ''' 
    Creates a folder for each file, naming the folder 
    the same name as the file and moving it into it 
    '''

    def __init__(self):
        '''
        Select the local of folder and determine the number of files in the folder (-1, then App.py don't count)
        '''
        self.folder = os.chdir(os.path.abspath(''))
        self.len_folder = int(len(os.listdir())-1)
        self.create_folders()

    def create_folders(self):
        ''' 
        Create a folder for each file with aleatory name (ZZZ 0, ZZZ 1, ZZZ2, ...)
        '''
        for i in range(0, self.len_folder):
            num = str(i)
            name = 'ZZZ ' + num
            os.makedirs(name)
        self.create_folders()

    def create_folders(self):
        ''' Rename the folders with the filename and move the file to the folder '''
        len_folder = self.len_folder
        for file_name in os.listdir()[0:len_folder]:
            # Old name receives the name of previously created folders (ZZZ 0, ZZZ 1, ...)
            old_name = os.listdir()[len_folder]
            new_name = file_name  # New nareceive the name of file
            leng = len(new_name)-4  # Lenght of new nameme
            shutil.move(new_name, old_name)  # Move file to folder
            # Rename folder with the name of file (no extension)
            os.rename(old_name, new_name[:leng])


class CreateFolder_CopyFiles:
    ''' Creates a folder for each file, naming the folder the same name as the 
        file and moving this file and more two file (expecifics for the all folders)    
    All itens:
        - App.py
        - City Base (.dwg) Drawing of city
        - Final project file with generic name (.dwg) (Expecific for the all folders)
        - Generic named Project data file (.xlsx) (Expecifics for the all folders)
        - Project file to do (.kmz) (Same name as the folder that will be created)    
    '''

    def __init__(self):
        '''
        Select the local of folder and determine the number of files in the folder (-1, then App.py don't count)
        '''
        self.local = os.path.abspath('')
        self.folder = os.chdir(self.local)
        self.len_folder = int(len(os.listdir())-1)
        self.decision()

    def decision(self):
        '''
        Projects have two types of names, 22000 or SV22000, if the projects 
        are 22000, the first file will be project 22000, otherwise the first 
        file will be City Base (because of the order). 
        '''
        firt_file = os.listdir()[0]
        decision_ = firt_file[0]
        if decision_ == 'b' or decision_ == 'B':
            self.create_copy_SV()
        else:
            self.create_copy_22()

    def create_copy_SV(self):
        for i in range(3, self.len_folder):
            # Create folder and define the files
            os.makedirs('ZZZZ')
            folder_ = os.listdir()[-2]
            dwg_out = os.listdir()[1]
            xml_out = os.listdir()[2]
            kmz_out = os.listdir()[i]

            # Copy files to folder
            shutil.copy(dwg_out, folder_)
            shutil.copy(xml_out, folder_)
            shutil.move(kmz_out, folder_)

            # Rename the folder
            name_folder_old = len(kmz_out)-4
            name_folder = kmz_out[:name_folder_old]
            os.rename(folder_, name_folder)

            # Enter in the new folder
            new_local = self.local + '/' + name_folder
            os.chdir(new_local)

            # Rename generic files with extension
            dwg = os.listdir()[0]
            xls = os.listdir()[1]
            os.rename(dwg, name_folder + '.dwg')
            os.rename(xls, name_folder + '.xls')

            # Return to main folder
            os.chdir(self.local)

    def create_copy_22(self):
        for i in range(2, self.len_folder-1):
            # Create folder and define the files
            os.makedirs('ZZZZ')
            folder_ = os.listdir()[self.len_folder]
            dwg_out = os.listdir()[0]
            xml_out = os.listdir()[1]
            kmz_out = os.listdir()[i]

            # Copy files to folder
            shutil.copy(dwg_out, folder_)
            shutil.copy(xml_out, folder_)
            shutil.move(kmz_out, folder_)

            # Rename the folder
            name_folder_old = len(kmz_out)-4
            name_folder = kmz_out[:name_folder_old]
            os.rename(folder_, name_folder)

            # Enter in the new folder
            new_local = self.local + '/' + name_folder
            os.chdir(new_local)

            # Rename generic files with extension
            dwg = os.listdir()[0]
            xls = os.listdir()[1]
            os.rename(dwg, name_folder + '.dwg')
            os.rename(xls, name_folder + '.xls')

            # Return to main folder
            os.chdir(self.local)


def select():
    '''
    Select the function
    '''
    text_answer["text"] = "Função executada com sucesso !"
    option = var.get()

    if option == 1:
        rename = CreatesFolder_MoveFile()
        rename.create_folders()
        rename.rename_and_move()
    elif option == 2:
        CreateFolder_CopyFiles()


'''
User interface
'''

window = Tk()
window.title("App para criação de pastas")

var = IntVar()

text_orientation1 = Radiobutton(
    window, text="Cria uma pasta com o mesmo nome do arquivo kmz e move o arquivo para dentro da pasta.", justify=LEFT, variable=var, value=1)
text_orientation1.grid(column=0, row=0, padx=15, pady=20)

text_orientation2 = Radiobutton(
    window, text="Cria uma pasta com o mesmo nome do arquivo kmz, move os arquivos kmz, dwg e xlsx para\ndentro da pasta e renomeia todos arquivos.", justify=LEFT, variable=var, value=2)
text_orientation2.grid(column=0, row=1, padx=15, pady=5)

button1 = Button(window, text="Clique para executar a ação", command=select)
button1.grid(column=0, row=2, pady=20)

text_answer = Label(window, text="")
text_answer.grid(column=0, row=3, pady=5)

window.mainloop()
