import os.path
import io
import codecs
from nt import listdir
folderName = "G:\STUDY\MS in CS\Spring 2017\CS522 ADM\Project\output.zip (Unzipped Files)\\"
file_list = [f for f in listdir(folderName)]
print(len(file_list))

outputfolder="G:\STUDY\MS in CS\Spring 2017\CS522 ADM\Project\Snippets"

#writeFile = open("G:\STUDY\MS in CS\Spring 2017\CS522 ADM\Project\Snippets.txt","w",encoding='utf-8')

for txtfile in file_list:
    #writeFile.write(txtfile)
    with io.open(folderName + txtfile,'r',encoding='utf-8') as tfile:
        counter = 0
        #print(txtfile)
        prevLine = ''
        nextLine = ''
        temp = ''
        prevLineContained = 0
        try:
            lines = tfile.readlines()
            for i,line in enumerate(lines):
                #decodedLine = line.decode('utf-8')
                """
                if prevLineContained is 1:
                    writeFile.write("Prev Line : " + prevLine)
                    writeFile.write("Next Line : " + line)
                    writeFile.write('\n')
                    prevLineContained = 0
                prevLine = temp
                temp = line
                if "Chicago school" in line:
                    prevLineContained = 1
                    writeFile.write("Found in " + txtfile + '\n')
                    writeFile.write("Line : " + line)
                """
                if "Chicago school" in line or "Chicago School" in line:
                    for c in line:
                        c.encode('utf-8')
                    counter = counter + 1
                    #print("i : ",i)
                    #print("found")
                    if "Chicago school" in line:
                        thisline = line.split("Chicago school")
                    else:
                        thisline = line.split("Chicago School")
                    #for item in thisline:
                        #print(item)
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
                    #print(len(prevWords))
                    #print(len(nextWords))
                    snippet = ' '.join(reversed(prevWords)) + " Chicago School" + ' '.join(nextWords)
                    #print(snippet)
                    fileName = outputfolder + \
                                "\\" + \
                                 txtfile + \
                                 "__" + \
                                 str(counter)
                    with io.open(fileName,'w+',encoding='utf-8') as writeFile:
                        #writeFile.write("-------Snippet Starting-------\n")
                        writeFile.write(snippet + '\n') 
                    #WriteFile.close()          
        except Exception as e:
            print("Caught an exception")
            #print(e.print_all())
            continue
#writeFile.close()

snippet_list = [f for f in listdir(outputfolder)]
print(len(snippet_list))
print("done")
            
            
        