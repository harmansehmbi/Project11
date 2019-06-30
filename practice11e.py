class CA:
    pass

cRef = CA()          # cRef is not an object
print("Object Data: ", cRef.__dict__)
print("Class Data: ", CA.__dict__)