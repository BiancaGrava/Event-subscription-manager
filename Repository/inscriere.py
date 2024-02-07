from Exceptii import RepoError
from Domain import Om
from Domain import Evenimente
from Domain import Inscrieri
class InscrieriRepo:
    def __init__(self):
        self._inscrieri=[]
    def cauta_ins(self, ins):
        # note este de tipul NOTE
        for n in self._inscrieri:
            if n == ins:
                return n
        return None

    def cautare_dupa_id(self, id_om,id_ev):
        for x in self._inscrieri:
            if x.get_persoana().get_id()==id_om and x.get_ev().get_id_ev()==id_ev:
                return x
        return None

    def add_ins(self, ins):
        for n in self._inscrieri:
            if n == ins:
                raise Exception("confirmarea participarii la eveniment a fost deja realizata pentru combinatia data persoana-eveniment")
        self._inscrieri.append(ins)

    def get_all(self):
        return self._inscrieri

    def __len__(self):
        return len(self._inscrieri)

class FileInsRepo(InscrieriRepo):
    def __init__(self, cale_fisier):
        InscrieriRepo.__init__(self)
        self.__cale_fisier = cale_fisier

    def __read_all_insc_from_file(self):
        with open(self.__cale_fisier, "r") as f:
            self._inscrieri.clear()
            lines = f.readlines()
            for line in lines:
                if line != "":
                    parts = line.split(" ")
                    if len(parts) == 8:#8
                        id_om = int(parts[0])
                        nume = parts[1]
                        adresa = parts[2]
                        id_ev = int(parts[3])
                        data = parts[4]
                        timp=parts[5]
                        desc = parts[6]
                        nr_pers = int(parts[7])
                        om = Om(id_om, nume, adresa)
                        ev = Evenimente(id_ev, data,timp,desc)
                        elem = Inscrieri(om, ev, nr_pers)
                        self._inscrieri.append(elem)


    def __write_all_insc_to_file(self):
        with open(self.__cale_fisier,"w") as f:
            for ins in self._inscrieri:
                f.write(str(ins)+"\n")

    def golire(self):
        with open(self.__cale_fisier, "w") as f:
            f.write("")

    def add_ins(self, ins):
        self.__read_all_insc_from_file()
        InscrieriRepo.add_ins(self, ins)
        self.__write_all_insc_to_file()

    def cautare_dupa_id(self, id_om, id_ev):
        self.__read_all_insc_from_file()
        return InscrieriRepo.cautare_dupa_id(self, id_om,id_ev)

    def get_all(self):
        self.__read_all_insc_from_file()
        return InscrieriRepo.get_all(self)

    def __len__(self):
        self.__read_all_insc_from_file()
        return InscrieriRepo.__len__(self)

