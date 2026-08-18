from tkinter.font import names


class MarksheetBean :
    def __init__(self):
        self.__id=0
        self.__rollno = 0
        self.__name=''
        self.__physics=0
        self.__chemistry=0
        self._maths=0
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id
    def set_rollno(self,rollno):
        self.__rollno=rollno
    def get_rollno(self):
        return self.__rollno
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_physics(self,physics):
        self.__physics=physics
    def get_physics(self):
        return self.__physics
    def set_chemistry(self,chemistry):
        self.__chemistry=chemistry
    def get_chemistry(self):
        return self.__chemistry
    def set_maths(self,maths):
        self.__maths=maths
    def get_maths(self):
        return self.__maths
