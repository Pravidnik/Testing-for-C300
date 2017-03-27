class MyMetaClass(type):

    def __new__(cls, name, bases, dct):
        dct['COLLECTION'] = name.capitalize()
        new_class = super(MyMetaClass, cls).__new__(cls, name, bases, dct)
        return new_class

class mycollection1(metaclass = MyMetaClass):
    pass


class mycollection2(metaclass = MyMetaClass):
    pass


print(mycollection1.COLLECTION)
print(mycollection2.COLLECTION)