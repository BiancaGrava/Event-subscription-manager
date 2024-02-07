from Domain import Evenimente
class EventRepository:

    def __init__(self):
        self._evenimente = {}

    def add_event(self,ev):
        '''
        adauga un eveniment in lista de evenimente
        :param ev: eveniment
        - modifica lista astfel incat evenimentul sa fie adaugat
        '''
        id_ev = ev.get_id_ev()
        if id_ev in self._evenimente.keys():
            raise Exception("id-ul exista deja!")
        self._evenimente[id_ev] = ev

    def delete_ev(self,id):
        '''
        stergere eveniment dupa id din lista de evenimente
        :param id: id
        :return: lista nou generata
        '''
        if id in self._evenimente.keys():
            for i in self._evenimente.keys():
                if id==self._evenimente[i].get_id_ev():
                    self._evenimente.pop(i)
                    return [self._evenimente[x] for x in self._evenimente.keys()]
        else:
            raise Exception("nu exista id!")

    def modifica_ev(self, eveniment):
        '''
        modifica evenimentul de la id ul evenimentului dat cu noile date din obiectul dat
        :param eveniment: eveniment nou
        :return: lista nou generata
        '''
        id_eveniment = eveniment.get_id_ev()
        data=eveniment.get_data()
        timp = eveniment.get_timp()
        descriere = eveniment.get_descriere()
        if self.cauta_elem(id_eveniment) == 1:
            for key in list(self._evenimente.keys()):
                if self._evenimente[key].get_id_ev() == id_eveniment:
                    self._evenimente[key].set_data(data)
                    self._evenimente[key].set_timp(timp)
                    self._evenimente[key].set_descriere(descriere)
        else:
            raise Exception("nu exista id!\n")

    def cauta_elem(self, id_eveniment):
        '''
        cauta obiectul dupa id ul sau in lista de evenimente
        :param id_eveniment: id
        :return: 0 sau 1 daca elementul este gasit sau nu
        '''
        for key in list(self._evenimente.keys()):
            if self._evenimente[key].get_id_ev() == id_eveniment:
                return 1
        return 0

    def cauta_id_ev(self, id):
        '''
        cauta u eveniment dupa id in lista si in cazul in care acesat exista in lista, este returnat
        :param id: id
        :return: evenimentul cautat
        '''

        if self.cauta_elem(id) == 1:
            for key in list(self._evenimente.keys()):
                if self._evenimente[key].get_id_ev() == id:
                    return self._evenimente[key]
        else:
            raise Exception("nu exista id!\n")

    def get_all(self):
        '''returneaza toata lista de evenimente'''
        return [self._evenimente[x] for x in self._evenimente.keys()]

    def __len__(self):
        return len(self._evenimente)

class FileEvRepo(EventRepository):

    def __init__(self, cale_fisier):
        EventRepository.__init__(self)
        self.__cale_fisier = cale_fisier

    def __read_all_events_from_file(self):
        with open(self.__cale_fisier, "r") as f:
            self._evenimente.clear()
            lines = f.readlines()
            for line in lines:
                if line != "":
                    parts = line.split(" ")
                    if len(parts) == 4:
                        id_ev = int(parts[0])
                        data = parts[1]
                        timp = parts[2]
                        descriere=parts[3]
                        ev = Evenimente(id_ev, data, timp, descriere)
                       # eveniment = Evenimente(id_ev, data, timp,descriere)
                        self._evenimente[id_ev] = ev

    def __write_all_events_to_file(self):
        with open(self.__cale_fisier,"w") as f:
            for id in self._evenimente.keys():
                f.write(str(self._evenimente[id])+"\n")

    def golire(self):
        with open(self.__cale_fisier,"w") as f:
            f.write("")

    def add_event(self,ev):
        self.__read_all_events_from_file()
        EventRepository.add_event(self,ev)
        self.__write_all_events_to_file()

    def delete_ev(self,id):
        '''
        stergere eveniment dupa id din lista de evenimente
        :param id: id
        :return: lista nou generata
        '''
        self.__read_all_events_from_file()
        EventRepository.delete_ev(self, id)
        self.__write_all_events_to_file()

    def modifica_ev(self, eveniment):
        '''
        modifica evenimentul de la id ul evenimentului dat cu noile date din obiectul dat
        :param eveniment: eveniment nou
        :return: lista nou generata
        '''
        self.__read_all_events_from_file()
        EventRepository.modifica_ev(self, eveniment)
        self.__write_all_events_to_file()

    def cauta_id_ev(self, id):
        '''
        cauta u eveniment dupa id in lista si in cazul in care acesat exista in lista, este returnat
        :param id: id
        :return: evenimentul cautat
        '''
        self.__read_all_events_from_file()
        return EventRepository.cauta_id_ev(self, id)

    def get_all(self):
        self.__read_all_events_from_file()
        return EventRepository.get_all(self)

    def __len__(self):
        self.__read_all_events_from_file()
        return EventRepository.__len__(self)