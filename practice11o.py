file  = open("practice11a.py", "r")
data = file.read(15)                        # read 15 characters
print(data)

print("++++++++++++++++++++++++++++++++++++")

file  = open("practice11a.py", "r")
data = file.read(30)                       # read 30 characters
print(data)

print("======================================")
data = file.read()                         # read after 30 characters
print(data)

print("Is File Closed:", file.closed)

file.close()   # Explicitly we are closing the file

print("Is File Closed:", file.closed)
