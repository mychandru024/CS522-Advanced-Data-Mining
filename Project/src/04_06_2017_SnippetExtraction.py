import os.path
import io
import codecs
from nt import listdir
folderName = "G:\STUDY\MS in CS\Spring 2017\CS522 ADM\Project\output.zip (Unzipped Files)\\"
file_list = [f for f in listdir(folderName)]
print(len(file_list))

outputfolder="G:\STUDY\MS in CS\Spring 2017\CS522 ADM\Project\Snippets"

for txtfile in file_list:
    with io.open(folderName + txtfile,'r',encoding='utf-8') as tfile:
        counter = 0
        prevLine = ''
        nextLine = ''
        temp = ''
        prevLineContained = 0
        try:
            lines = tfile.readlines()
            #lines = lines_raw.decode('utf-8')
            #print("File length : ", len(lines))
            for i,line in enumerate(lines):
                if "Chicago school" in line or "Chicago School" in line:
                    for c in line:
                        c.encode('utf-8')
                    counter = counter + 1
                    if "Chicago school" in line:
                        thisline = line.split("Chicago school")
                    else:
                        thisline = line.split("Chicago School")

                    prevWords = []
                    #finding previous 20 characters
                    for k in reversed(thisline[0].split(" ")):
                        prevWords.append(k)
                    j = i - 1
                    while j > 0 and len(prevWords) < 20:
                        words = reversed(lines[j].split(" "))
                        j = j - 1
                        for word in words:
                            for c in word:
                                c.encode('utf-8')
                            prevWords.append(word)
                            if len(prevWords) >= 20:
                                break
                    
                    
                    nextWords = []
                    #finding previous 20 characters
                    for k in thisline[1].split(" "):
                        nextWords.append(k)
                    j = i + 1
                    while j < len(lines) and len(nextWords) < 20:
                        words = lines[j].split(" ")
                        j = j + 1
                        for word in words:
                            for c in word:
                                c.encode('utf-8')
                            nextWords.append(word)
                            if len(nextWords) >= 20:
                                break
                    fileParts = txtfile.split(".")
                    snippet = ' '.join(reversed(prevWords)) + " Chicago School" + ' '.join(nextWords)
                    fileName = outputfolder + \
                                "\\" + \
                                 fileParts[0] + \
                                 "." + fileParts[1] + \
                                 "__" + \
                                 str(counter) + \
                                 "." + fileParts[2]
                                 
                    with io.open(fileName,'w+',encoding='utf-8') as writeFile:
                        writeFile.write(snippet + '\n')        
        except Exception as e:
            print(txtfile)
            print("Caught an exception")
            #print(e.print_all())
            continue
snippet_list = [f for f in listdir(outputfolder)]
print(len(snippet_list))
print("done")
            
            
        