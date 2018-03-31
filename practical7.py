#create directory
import os
if not os.path.exists("directory"):
    os.makedirs("directory")
#rename a file
os.rename('demo.txt','demos.txt')
#delete directory
os.rmdir("directory")
