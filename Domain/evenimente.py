class Evenimente:
    def __init__(self, id_ev, data, timp,descriere):
        '''
        creeaza obiectul studenti pentru a putea fi folosit in service
        '''
        self.__id_ev=id_ev
        self.__data=data
        self.__timp=timp
        self.__descriere=descriere

    def get_id_ev(self):
        return self.__id_ev

    def get_data(self):
        return self.__data

    def get_timp(self):
        return self.__timp

    def get_descriere(self):
        return self.__descriere

    def set_id_ev(self, new_id):
        self.__id_ev=new_id

    def set_data(self, new_data):
        self.__data=new_data

    def set_timp(self, new_timp):
        self.__timp = new_timp

    def set_descriere(self, new_descriere):
        self.__descriere=new_descriere

    def __eq__(self,gi):
        return self.__id_ev == gi.__id_ev

    def __str__(self):
        return f"{self.__id_ev} {self.__data} {self.__timp} {self.__descriere}"
        #return f"ID: {self.__id_ev}, DATA: {self.__data}, TIMP: {self.__timp}, DESCRIERE: {self.__descriere}"

    #def creeaza_om(id, nume, adresa):
    #    return {'id': id, 'nume': nume, 'adresa': adresa}
