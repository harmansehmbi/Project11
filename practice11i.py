# object is parent by default...


class CA(object):
    pass

cRef = CA()
print("Object Data: ", cRef.__dict__)
print("Class Data: ", CA.__dict__)