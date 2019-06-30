file  = open("practice11a.py", "r")
print(type(file))

fileContents =file.read()
print(type(fileContents))

print()

print(fileContents)
print(len(fileContents))

print(">> Re Read File")

# Re-Read the File
fileContents = file.read()   # Re-Read
print(fileContents)

# Once a file is opened and read we can not read it !!
# We need to re-open and re-read

