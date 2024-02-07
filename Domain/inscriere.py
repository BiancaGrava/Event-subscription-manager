from Domain import Om
from Domain import Evenimente
class Inscrieri:
    def __init__(self,persoana,eveniment,nr_pers):
        self.__persoana=persoana
        self.__eveniment=eveniment
        self.__nr_pers=nr_pers

    def get_persoana(self):
        return self.__persoana

    def get_ev(self):
        return self.__eveniment

    def get_nrp(self):
        return self.__nr_pers

    def set_nrp(self,nr):
        self.__nr_pers=nr

    def set_persoana(self,pers):
        self.__persoana.set_nume(pers.get_nume())
        self.__persoana.set_id(pers.get_id())
        self.__persoana.set_adresa(pers.get_adresa())

    def set_ev(self,ev):
        self.__eveniment.set_id_ev(ev.get_id_ev())
        self.__eveniment.set_data(ev.get_data())
        self.__eveniment.set_timp(ev.get_timp())
        self.__eveniment.set_descriere(ev.get_descriere())

    def __eq__(self, gi):
        """
        asocierea dintre eveniment si persoana e unica
        """
        if gi==None:
            return False
        else:
            return self.__eveniment==gi.get_ev() and self.__persoana==gi.get_persoana()

    def __str__(self):
        return f"{str(self.__persoana).strip()} {str(self.__eveniment).strip()} {self.__nr_pers}"
        #return f"NUME PERSOANA: {self.__persoana.get_nume()}, EVENIMENT: {self.__eveniment.get_id_ev()}, {self.__eveniment.get_descriere()}, +{self.__nr_pers}"

def testCreateInscriere():
    persoana=Om(12,"a-a","str.1,nr.2")
    eveniment=Evenimente(13,"12/02/2024","12:00","majorat")
    inscriere=Inscrieri(persoana,eveniment,2)
    assert inscriere.get_ev()==eveniment
    assert inscriere.get_persoana()==persoana
    assert inscriere.get_nrp()==2

testCreateInscriere()

class EvenimentInscriere:
    """Data Transfer Object"""
    def __init__(self,omID, id_ev,descriere, data,nr_pers):
        self.__omID = omID
        self.__id_ev = id_ev
        self.__descriere = descriere
        self.__data=data
        self.__nr_pers=nr_pers
        self.__name = None

    def getOmID(self):
        """
         Getter method
        """
        return self.__omID
    def getEvID(self):
        """
         Getter method
        """
        return self.__id_ev
    def getDescriere(self):
        """
         Getter method
        """
        return self.__descriere

    def getData(self):
        """Getter method"""
        return self.__data
    def getPers(self):
        """
         Getter method
        """
        return self.__nr_pers

    def getOmName(self):
        """
         Getter method
        """
        return self.__name

    def setOmName(self,n):
        self.__name = n

    def __str__(self):
        return f"ID PERSOANA: {self.__omID}; EVENIMENT: {self.__id_ev}, {self.__descriere.strip()}, {self.__data}; +{self.__nr_pers}"


def testEvenimentInscriere():
    sg = EvenimentInscriere(1,2,"majorat","12/03/2024",2)
    assert sg.getOmID()==1
    assert sg.getEvID() == 2
    assert sg.getDescriere()=="majorat"
    assert sg.getData()=="12/03/2024"
    assert sg.getPers()==2

testEvenimentInscriere()