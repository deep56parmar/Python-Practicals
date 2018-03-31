#Copy from one file to another file
fileHandler = open("demo.txt",'w')
fileHandler.write("\n Hello, My name is Deep Parmar. \n Nice to meet you. \n Bye, Thank you.")
string = ""
fileHandler.close()
fileHandler = open("demo.txt",'r')
for line in fileHandler:
    string += fileHandler.read()
fileHandler.close()
fileHandler = open("test.txt",'w')
fileHandler.write(string)
fileHandler.close()

#Append in one file.
fileHandler = open("demo.txt",'a')
fileHandler.write("Adios Amigos!!!")
fileHandler.close()
