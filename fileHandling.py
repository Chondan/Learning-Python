class FileHandling:
    fileDirectory = None
    isFileClose = False
    f = None
    def __init__(self, fileDirectory):
        self.fileDirectory = fileDirectory
        
    def openFile(self):
        try:
            self.f = open(self.fileDirectory, "r")
            self.isFileClose = False
            print("The file was opened")
            return self.f
        except:
            print("The file does not exist")

    # You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file
    def closeFile(self):
        self.f.close()
        self.isFileClose = True

    def readFile(self):
        f = self.openFile()
        print(f.read())
        self.closeFile()

    def readFileSomePart(self, length):
        f = self.openFile()
        print(f.read(length))
        self.closeFile()
    
    def readLineFile(self):
        if (self.isFileClose):
            f = self.openFile()
        try:
            print(self.f.readline())
        except:
            print("Reach the end of the file")

    def loopThroughFile(self):
        f = self.openFile()
        for x in f:
            print(x)
    # File Write
    # To write an existing file, you must add a parameter to the open() function
    # 'a' - Append - will append to the end of the file
    # 'w' - Write - will overwrite any existing content
    def writeFile(self, content):
        f = open(self.fileDirectory, "a")
        f.write(content)
        f.close()
    def overwriteFile(self, content):
        f = open(self.fileDirectory, "w")
        f.write(content)
        f.close()
    def deleteFile(self):
        import os
        # --- Check if File exist
        if (os.path.exists(self.fileDirectory)):
            os.remove(self.fileDirectory)
        else:
            print("The file does not exist");
    def createFile(self):
        open(self.fileDirectory, "w");
    def createFolder(self):
        import os
        os.mkdir(self.fileDirectory)
    def deleteFolder(self):
        import os
        os.rmdir(self.fileDirectory)
        
# file1 = FileHandling("./txt/file2.txt")
# file1.readFile()
# file1.readFileSomePart(5)
# file1.readLineFile()
# file1.readLineFile()
# file1.closeFile()
# file1.readLineFile()
# file1.readLineFile()
# # file1.readLineFile()
# file1.loopThroughFile()
# file1.writeFile("\nHow are you?")
# file1.overwriteFile("Oops, I have deleted the content!");

# ----- Create a New File
# f = open("./txt/file3.txt", "x"); # Create a file, returns an error if the file exist
# f = open("./txt/file3.txt", "w"); # Create a file if the specified file does not exist
# file = FileHandling("./txt/file3.txt");
# file.createFile();
# file.writeFile("Hello, I am Chondan Susuwan");
# file.deleteFile();

file = FileHandling("./newfolder/");
# file.createFolder();
file.deleteFolder();