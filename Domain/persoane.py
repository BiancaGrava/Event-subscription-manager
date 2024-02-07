class Om:
    def __init__(self, id, nume, adresa):
        '''
        creeaza obiectul dtudenti pentru a putea fi folosit in service
        '''
        self.__id=id
        self.__nume=nume
        self.__adresa=adresa
        #self.date={'id': id, 'nume': nume, 'adresa': adresa}

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_adresa(self):
        return self.__adresa

    def set_id(self, new_id):
        self.__id=new_id

    def set_nume(self, new_nume):
        self.__nume = new_nume

    def set_adresa(self, new_adresa):
        self.__adresa=new_adresa

    def __eq__(self,gigi):
        return self.__id == gigi.get_id()

    def __str__(self):
        return f"{self.__id} {self.__nume} {self.__adresa}"
        #return f"ID: {self.__id}, NUME: {self.__nume}, ADRESA: {self.__adresa}"

    #def creeaza_om(id, nume, adresa):
    #    return {'id': id, 'nume': nume, 'adresa': adresa}
