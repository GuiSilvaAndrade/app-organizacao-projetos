import os
import shutil
#import requests
from tkinter import *
import customtkinter


class App1():
    def __init__(self):
        """Start"""
        self.address = os.path.abspath('') # File address
        os.chdir(self.address) # Access the new Address 
        
        listFiles = os.listdir() # List of files
        numFilesIni = len(listFiles) # Number of files
        self.numFiles = int(numFilesIni) - 1 # Number of files in the folder (except the executable)
        self.foldersForCorrection()      

    def foldersForCorrection(self):
        for i in range(0, self.numFiles):
            os.makedirs('XYZ') # Create generic folder
            newFolderName = os.listdir()[i] # Select file name
            shutil.move(newFolderName, 'XYZ') # Move file to folder

            aux = len(newFolderName)-4 # Remove extension and dot
            newNewFolderName = newFolderName[:aux] # Remove extension and dot

            os.rename('XYZ', newNewFolderName) # Rename folder to new name
         

class App2():
    def __init__(self):
        """Start"""
        self.address = os.path.abspath('') # File address
        os.chdir(self.address) # Access the new Address 

        self.nameFolder = '002. Enviar via e-mail' # Folder name
        os.makedirs(self.nameFolder) # Create folder 

        listFiles = os.listdir() # List of files
        numFilesIni = len(listFiles) # Number of files
        self.numFiles = int(numFilesIni) - 1 # Number of files in the folder (except the executable)
        self.whichCompany()
        
    def whichCompany(self):
        """decides if they are SOLVE or MERCOSOL projects (Base ou 23000)"""
        firt_file = os.listdir()[1] # Name of the first file, except for the one created folder
        characterName = firt_file[0] # Firt character of first file

        if characterName == 'b' or characterName == 'B': # Initial file is Base
            self.separateInFoldersSolve()
            self.folderForEmailSolve()
        else: 
            # Initial file is 23000
            self.separateInFoldersMercosol()
            self.folderForEmailMercosol()
    
    def separateInFoldersSolve(self):                
        for _ in range(2, self.numFiles + 1): # Move the files to the folder (except folder)
            curretFile = os.listdir()[1] # Select current file
            shutil.move(curretFile, self.nameFolder) # Move

    def separateInFoldersMercosol(self):  
        for _ in range(2, self.numFiles + 1): # Move the files to the folder (except folder)
            curretFile = os.listdir()[1] # Select current file
            shutil.move(curretFile, self.nameFolder) # Move
        
    def folderForEmailSolve(self):
        os.chdir(self.address)
        selectFolder = os.listdir()[0] # Select folder
        newAddress = os.path.abspath(selectFolder) # Increment the address
        os.chdir(newAddress) # Access the new Address 

        listFilesEmail = os.listdir() # List of files
        numFilesEmail = len(listFilesEmail) # Number of files
        
        for i in range(3, numFilesEmail):   
            file_dwg = os.listdir()[1]
            file_xls = os.listdir()[2]
            newFolderName = os.listdir()[i] # Select file name

            os.makedirs('XYZ') # Create generic folder
            
            shutil.move(newFolderName, 'XYZ') # Move file to folder
            shutil.copy(file_dwg, 'XYZ') # Copy file to folder
            shutil.copy(file_xls, 'XYZ') # Copy file to folder

            newNewAddress = os.path.abspath('XYZ') # Increment the address
            os.chdir(newNewAddress) # Access the new Address 

            aux = len(newFolderName)-4 # Remove extension and dot
            newNewFolderName = newFolderName[:aux] # Remove extension and dot
            
            os.rename(os.listdir()[0], newNewFolderName + '.dwg') # Rename first file 
            os.rename(os.listdir()[0], newNewFolderName + '.xls') # Rename first file 
            
            backToFolder = os.path.abspath(r'../') # Decrement the address
            os.chdir(backToFolder) # Access the new Address 
            
            os.rename('XYZ', newNewFolderName) # Rename folder
            
    def folderForEmailMercosol(self): 
        os.chdir(self.address)
        selectFolder = os.listdir()[0] # Select folder
        newAddress = os.path.abspath(selectFolder) # Increment the address
        os.chdir(newAddress) # Access the new Address 

        listFilesEmail = os.listdir() # List of files
        numFilesEmail = len(listFilesEmail) # Number of files
        
        for i in range(2, numFilesEmail - 1):   
            file_dwg = os.listdir()[0]
            file_xls = os.listdir()[1]
            newFolderName = os.listdir()[i] # Select file name

            os.makedirs('XYZ') # Create generic folder
            
            shutil.move(newFolderName, 'XYZ') # Move file to folder
            shutil.copy(file_dwg, 'XYZ') # Copy file to folder
            shutil.copy(file_xls, 'XYZ') # Copy file to folder

            newNewAddress = os.path.abspath('XYZ') # Increment the address
            os.chdir(newNewAddress) # Access the new Address 

            aux = len(newFolderName)-4 # Remove extension and dot
            newNewFolderName = newFolderName[:aux] # Remove extension and dot
            
            os.rename(os.listdir()[0], newNewFolderName + '.dwg') # Rename first file 
            os.rename(os.listdir()[0], newNewFolderName + '.xls') # Rename first file 
            
            backToFolder = os.path.abspath(r'../') # Decrement the address
            os.chdir(backToFolder) # Access the new Address 
            
            os.rename('XYZ', newNewFolderName) # Rename folder


class App3():
    def __init__(self):
        """Start"""
        self.address = os.path.abspath('') # File address
        os.chdir(self.address) # Access the new Address 
        
        self.nameFolder1 = '0. Correção - Á FAZER' # Folder name
        self.nameFolder2 = '0. Projetos' # Folder name
        os.makedirs(self.nameFolder1) # Create folder 
        os.makedirs(self.nameFolder2) # Create folder 

        listFiles = os.listdir() # List of files
        numFilesIni = len(listFiles) # Number of files
        self.numFiles = int(numFilesIni) - 1 # Number of files in the folder (except the executable)
        self.whichCompany()
        
    def whichCompany(self):
        """decides if they are SOLVE or MERCOSOL projects (Base ou 23000)"""
        firt_file = os.listdir()[2] # Name of the first file, except for the two created folders
        characterName = firt_file[0] # Firt character of first file

        if characterName == 'b' or characterName == 'B': # Initial file is Base         
            self.separateInFoldersSolve()
            self.foldersForCorrection()
            self.folderForEmailSolve()
        else: 
            # Initial file is 23000
            self.separateInFoldersMercosol()
            self.foldersForCorrection()
            self.folderForEmailMercosol()
    
    def separateInFoldersSolve(self):         
        for i in range(5, self.numFiles): # Copy the files to the folder (except folder1, folder2, Base, SV23000.dwg, SV23000.xml)
            curretFile = os.listdir()[i] # Select current file
            shutil.copy(curretFile, self.nameFolder1) # Copy
        
        for j in range(3, self.numFiles + 1): # Move the files to the folder (except folder1, folder2)
            curretFile = os.listdir()[2] # Select current file
            shutil.move(curretFile, self.nameFolder2) # Move

    def separateInFoldersMercosol(self):  
        for i in range(4, self.numFiles - 1): # Copy the files to the folder (except folder1, folder2, 23000.dwg, 23000.xml and Base)
            curretFile = os.listdir()[i] # Select current file
            shutil.copy(curretFile, self.nameFolder1) # Copy
        
        for j in range(3, self.numFiles + 1): # Move the files to the folder (except folder1, folder2)
            curretFile = os.listdir()[2] # Select current file
            shutil.move(curretFile, self.nameFolder2) # Move

    def foldersForCorrection(self):
        selectFolder1 = os.listdir()[0] # Select folder 001
        newAddress = os.path.abspath(selectFolder1) # Increment the address
        os.chdir(newAddress) # Access the new Address 

        listFilesCorrection = os.listdir() # List of files
        numFilesCorrection = len(listFilesCorrection) # Number of files

        for i in range(0, numFilesCorrection):
            os.makedirs('XYZ') # Create generic folder
            newFolderName = os.listdir()[i] # Select file name
            shutil.move(newFolderName, 'XYZ') # Move file to folder

            aux = len(newFolderName)-4 # Remove extension and dot
            newNewFolderName = newFolderName[:aux] # Remove extension and dot

            os.rename('XYZ', newNewFolderName) # Rename folder to new name
        
    def folderForEmailSolve(self):
        os.chdir(self.address)
        selectFolder2 = os.listdir()[1] # Select folder 002
        newAddress = os.path.abspath(selectFolder2) # Increment the address
        os.chdir(newAddress) # Access the new Address 

        listFilesEmail = os.listdir() # List of files
        numFilesEmail = len(listFilesEmail) # Number of files
        
        for i in range(3, numFilesEmail):   
            file_dwg = os.listdir()[1]
            file_xls = os.listdir()[2]
            newFolderName = os.listdir()[i] # Select file name

            os.makedirs('XYZ') # Create generic folder
            
            shutil.move(newFolderName, 'XYZ') # Move file to folder
            shutil.copy(file_dwg, 'XYZ') # Copy file to folder
            shutil.copy(file_xls, 'XYZ') # Copy file to folder

            newNewAddress = os.path.abspath('XYZ') # Increment the address
            os.chdir(newNewAddress) # Access the new Address 

            aux = len(newFolderName)-4 # Remove extension and dot
            newNewFolderName = newFolderName[:aux] # Remove extension and dot
            
            os.rename(os.listdir()[0], newNewFolderName + '.dwg') # Rename first file 
            os.rename(os.listdir()[0], newNewFolderName + '.xls') # Rename first file 
            
            backToFolder = os.path.abspath(r'../') # Decrement the address
            os.chdir(backToFolder) # Access the new Address 
            
            os.rename('XYZ', newNewFolderName) # Rename folder
            
    def folderForEmailMercosol(self):
        os.chdir(self.address)
        selectFolder2 = os.listdir()[1] # Select folder 002
        newAddress = os.path.abspath(selectFolder2) # Increment the address
        os.chdir(newAddress) # Access the new Address 

        listFilesEmail = os.listdir() # List of files
        numFilesEmail = len(listFilesEmail) # Number of files
        
        for i in range(2, numFilesEmail - 1):   
            file_dwg = os.listdir()[0]
            file_xls = os.listdir()[1]
            newFolderName = os.listdir()[i] # Select file name

            os.makedirs('XYZ') # Create generic folder
            
            shutil.move(newFolderName, 'XYZ') # Move file to folder
            shutil.copy(file_dwg, 'XYZ') # Copy file to folder
            shutil.copy(file_xls, 'XYZ') # Copy file to folder

            newNewAddress = os.path.abspath('XYZ') # Increment the address
            os.chdir(newNewAddress) # Access the new Address 

            aux = len(newFolderName)-4 # Remove extension and dot
            newNewFolderName = newFolderName[:aux] # Remove extension and dot
            
            os.rename(os.listdir()[0], newNewFolderName + '.dwg') # Rename first file 
            os.rename(os.listdir()[0], newNewFolderName + '.xls') # Rename first file 
            
            backToFolder = os.path.abspath(r'../') # Decrement the address
            os.chdir(backToFolder) # Access the new Address 
            
            os.rename('XYZ', newNewFolderName) # Rename folder

             

def select():
    """Select the function"""
    text_answer["text"] = "Feito mô querido !"
    option = var.get()
        
    if option == 1:
        App1()
    elif option == 2:
        App2()
        pass
    elif option == 3:
        App3()




window = Tk()
window.title("Solve Automation")

var = IntVar()

text_orientation1 = Radiobutton(
    window, text="Cria uma pasta com o mesmo nome do arquivo kmz e move o arquivo para dentro da pasta.         ", justify=LEFT, variable=var, value=1)
text_orientation1.grid(column=0, row=0, padx=15, pady=20)

text_orientation2 = Radiobutton(
    window, text="Cria uma pasta com o mesmo nome do arquivo kmz, move os arquivos kmz, dwg e Anexo IV        \npara dentro da pasta, renomeia todos arquivos e copia uma versão da Base para todas as pastas.", justify=LEFT, variable=var, value=2)
text_orientation2.grid(column=0, row=1, padx=15, pady=0)

text_orientation3 = Radiobutton(
    window, text="Executa as duas opções anteriores em paralelo.                                                                                         ", justify=LEFT, variable=var, value=3)
text_orientation3.grid(column=0, row=2, padx=15, pady=15)

button1 = Button(window, text="Clique para gerar as pastas", command=select)
button1.grid(column=0, row=4, pady=20)

text_answer = Label(window, text="")
text_answer.grid(column=0, row=3, pady=5)



window.mainloop()


# py -m PyInstaller --onefile --noconsole __SolveApp__.py
# ou
# py -m PyInstaller --onefile --noconsole __SolveApp__.py

