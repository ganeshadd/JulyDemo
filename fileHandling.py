#Open File
file = open("Knowledg\\input.txt","r")

# Store content in variable 
content = file.read()

# close the connection/file
file.close()

print(content)