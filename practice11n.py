file  = open("practice11a.py", "r")

lines = file.readlines()
print(lines)
print(type(lines))

for line in lines:       # for reading line by line
    print(line)