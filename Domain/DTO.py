class EventDTO:
    def __init__(self,id_ev,descriere,nr_ins):
        self.__id_ev=id_ev
        self.__descriere=descriere
        self.__total_ins=nr_ins

    def get_id_dto_ev(self):
        return self.__id_ev
    def get_descriere_dto(self):
        return self.__descriere

    def mai_multe_inscrieri(self,nr_ins):
        self.__total_ins+=nr_ins


class PersDTO:
    def __init__(self,id_om,nume_om):
        self.__id_om=id_om
        self.__nume_om=nume_om
        self.__nr_ev=0

    def get_id_dto_om(self):
        return self.__id_om
    def get_nume_dto(self):
        return self.__nume_om

    def inc_ev(self):
        self.__nr_ev+=1


