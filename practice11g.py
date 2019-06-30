class CA:
    pass

class CB(CA):
    pass

class CC(CB):
    pass

cRef = CA()          # cRef is not an object
print("Object Data: ", cRef.__dict__)
print("Class Data: ", CA.__dict__)
print("child Class Data: ", CB.__dict__)
print("child Class Data: ", CC.__dict__)