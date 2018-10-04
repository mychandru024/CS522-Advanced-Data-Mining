import os.path
from nt import listdir
import json

#Folder containing the meta data files
metadataFolder = "G:\STUDY\MS in CS\Spring 2017\CS522 ADM\Project\JSON\metadata\meta\\"

#folders containing the text files
textFilesFolder = "G:\STUDY\MS in CS\Spring 2017\CS522 ADM\Project\output.zip (Unzipped Files)\\"

#take all the files in the text files folder
file_list = [f for f in listdir(textFilesFolder)]

#for each text file
for file in file_list:
    print("File to be renamed : ",file)
    fileNameParts = file.split(".")
    
    #corresponding meta data file
    corresponding_metadata_file_path = metadataFolder + fileNameParts[0] + "." + fileNameParts[1] + ".json"
    if not os.path.exists(corresponding_metadata_file_path):
        continue
    corresponding_metadata_file = open(corresponding_metadata_file_path)
    
    #read acs_data from the json file
    fileMetaData = json.load(corresponding_metadata_file)
    acs_date = fileMetaData["acsDate"] 
    print(fileMetaData["acsDate"])
    
    #constructing the new file name with acs_data prepended
    newFileName = acs_date + "_" + file
    print("New name : ",newFileName)
    
    #renaming the file
    os.rename(textFilesFolder + file,textFilesFolder + newFileName)
    corresponding_metadata_file.close()
print("Done")

