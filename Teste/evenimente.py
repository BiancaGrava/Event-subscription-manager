from Domain import Evenimente
from Validare import ValidatorEveniment
from Repository import EventRepository
from Repository import FileEvRepo
class TesteEvenimente:
    def __test_create_ev(self):
        id_ev = 9
        data = "12/04/2023"
        timp = "12:00"
        desc = "majorat"
        ev = Evenimente(id_ev, data, timp, desc)
        assert ev.get_id_ev() == id_ev
        assert ev.get_data() == data
        assert ev.get_timp() == timp
        assert ev.get_descriere() == desc

    def __test_validate_ev(self):
        id_ev = 9
        data = "12/04/2023"
        timp = "12:00"
        desc = "majorat"
        ev = Evenimente(id_ev, data, timp, desc)
        bad_id = -23
        bad_timp = "12"
        bad_data = "101/31/1800"
        descriere = "aa"
        bad_ev = Evenimente(bad_id, bad_data, bad_timp, descriere)
        validator = ValidatorEveniment()
        validator.valideaza_ev(ev)
        try:
            validator.valideaza_ev(bad_ev)
            assert False
        except Exception as ex:
            assert str(ex)=="id invalid!\neveniment incheiat!\nluna incorecta!\nformatul timpului invalid!\n"

    def __test_add_ev(self):
        id = 23
        nume = "12/03/2024"
        adresa = "00:00"
        des="aa"
        om = Evenimente(id, nume, adresa,des)
        repo=EventRepository()
        repo.add_event(om)

        id1 = 23
        nume1 = "12/03/2024"
        adresa1 = "00:00"
        des1 = "aa"
        ev = Evenimente(id1, nume1, adresa1,des1)
        repo = EventRepository()
        try:
            repo.add_event(ev)
        except Exception as ex:
            assert(str(ex)=="id-ul exista deja!")

    def __test_get_all(self):
        id = 23
        data = "12/02/2024"
        timp = "12:00"
        desc="a"
        ev = Evenimente(id, data, timp, desc)
        repo=EventRepository()
        repo.add_event(ev)
        assert repo.get_all()==[ev]

    def __test_add_and_get_all_file(self):
        repo = FileEvRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\persoane.txt")
        repo.golire()
        ev = Evenimente(12, "12/03/2024", "00:00", "majorat")
        repo.add_event(ev)
        assert repo.get_all() == [ev]

    def __test_modifica(self):
        repo = FileEvRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\evenimente.txt")
        repo.golire()
        ev = Evenimente(12, "12/03/2024", "00:00", "majorat")
        repo.add_event(ev)
        ev1=Evenimente(12,"12/03/2025","12:00","nuinevoie")
        repo.modifica_ev(ev1)
        assert repo.get_all() == [ev1]

    def __test_delete(self):
        repo = FileEvRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\evenimente.txt")
        repo.golire()
        ev = Evenimente(12, "12/03/2024", "00:00", "majorat")
        repo.add_event(ev)
        ev1 = Evenimente(13, "12/03/2025", "12:00", "nuinevoie")
        repo.add_event(ev1)
        repo.delete_ev(12)
        assert repo.get_all() == [ev1]

    def __test_cdi(self):
        repo = FileEvRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\evenimente.txt")
        repo.golire()
        ev = Evenimente(12, "12/03/2024", "00:00", "majorat")
        repo.add_event(ev)
        ev1 = Evenimente(13, "12/03/2025", "12:00", "nuinevoie")
        repo.add_event(ev1)
        assert repo.cauta_id_ev(12)==ev

    def erun_teste(self):
        self.__test_create_ev()
        self.__test_validate_ev()
        self.__test_add_ev()
        self.__test_get_all()
        self.__test_add_and_get_all_file()
        self.__test_modifica()
        self.__test_delete()
        self.__test_cdi()