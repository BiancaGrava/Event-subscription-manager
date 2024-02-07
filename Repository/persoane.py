from Exceptii import RepoError
from Domain import Om
class OmRepository:

    def __init__(self):
        self._oameni = {}

    def add_om(self,om):
        '''
                adauga om in lista de oameni
                :param id_baller: id
                :param name: nume
                :param value: adresa
                :return:
                '''
        id_om = om.get_id()
        if id_om in self._oameni.keys():
            raise RepoError("id-ul exista deja!")
        self._oameni[id_om] = om

    def delete_om(self,id):
        '''
                sterge din lista un om dupa id
                :param id:
                :return:
                '''
        if id in self._oameni.keys():
            for i in self._oameni.keys():
                if id==self._oameni[i].get_id():
                    self._oameni.pop(i)
                    return [self._oameni[x] for x in self._oameni.keys()]
        return [self._oameni[x] for x in self._oameni.keys()]

    def cauta_id(self, id):
        '''
                cauta in lista un om dupa id
                :param id: id
                :return: omul din lista, daca se afla in lista
                '''
        ok = 0
        try:
            return self._oameni[id]
            ok = 1
        except Exception:
            raise Exception("nu exista id!\n")
        if ok == 0:
            raise Exception("nu exista id!\n")

    def modifica_om(self, om):
        '''
                modifica un om din lista
                :param id: id
                :param nume: nume
                :param adresa: adresa
                :return: lista de oameni cu omul cu id ul id modificat cu noile date
                '''
        id_student = om.get_id()
        nume = om.get_nume()
        adresa = om.get_adresa()
        if self.cauta_elem(id_student) == 1:
            for key in list(self._oameni.keys()):
                if self._oameni[key].get_id() == id_student:
                    self._oameni[key].set_nume(nume)
                    self._oameni[key].set_adresa(adresa)
        else:
            raise Exception("nu exista id!\n")

    def cauta_elem(self, id_student):
        for key in list(self._oameni.keys()):
            if self._oameni[key].get_id() == id_student:
                return 1
        return 0

    def __len__(self):
        return len(self._oameni)
    def get_all(self):
        return [self._oameni[x] for x in self._oameni.keys()]

class FileOmRepo(OmRepository):

    def __init__(self, cale_fisier):
        OmRepository.__init__(self)
        self.__cale_fisier = cale_fisier

    def __read_all_people_from_file(self):
        with open(self.__cale_fisier, "r") as f:
            self._oameni.clear()
            lines = f.readlines()
            for line in lines:
                if line != "":
                    parts = line.split(" ")
                    if len(parts) == 3:
                        id_om = int(parts[0])
                        nume = parts[1]
                        adresa = parts[2]

                        om = Om(id_om, nume, adresa)
                       # eveniment = Evenimente(id_ev, data, timp,descriere)
                        self._oameni[id_om] = om

    def __write_all_people_to_file(self):
        with open(self.__cale_fisier,"w") as f:
            for id in self._oameni.keys():
                f.write(str(self._oameni[id])+"\n")

    def golire(self):
        with open(self.__cale_fisier,"w") as f:
            f.write("")

    def add_om(self,om):
        self.__read_all_people_from_file()
        OmRepository.add_om(self,om)
        self.__write_all_people_to_file()

    def delete_om(self,id):
        '''
                sterge din lista un om dupa id
                :param id:
                :return:
                '''
        self.__read_all_people_from_file()
        OmRepository.delete_om(self, id)
        self.__write_all_people_to_file()

    def cauta_id(self, id):
        '''
                cauta in lista un om dupa id
                :param id: id
                :return: omul din lista, daca se afla in lista
                '''
        self.__read_all_people_from_file()
        return OmRepository.cauta_id(self, id)

    def modifica_om(self, om):
        '''
                modifica un om din lista
                :param id: id
                :param nume: nume
                :param adresa: adresa
                :return: lista de oameni cu omul cu id ul id modificat cu noile date
                '''
        self.__read_all_people_from_file()
        OmRepository.modifica_om(self, om)
        self.__write_all_people_to_file()

    def get_all(self):
        self.__read_all_people_from_file()
        return OmRepository.get_all(self)

    def __len__(self):
        self.__read_all_people_from_file()
        return OmRepository.__len__(self)