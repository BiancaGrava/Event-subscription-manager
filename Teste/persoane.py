from Domain import Om
from Validare import ValidatorPersoana
from Repository import OmRepository
from Repository import FileOmRepo
class TestePersoane:
    def __test_create_om(self):
        id = 9
        nume = "Stefan-Vlad"
        adresa ="str.av,nr.12"
        om = Om(id,nume,adresa)
        assert om.get_id() == id
        assert om.get_nume() == nume
        assert om.get_adresa()==adresa

    def __test_validate_om(self):
        id = 23
        nume = "Marius-Marcel"
        adresa = "str.av,nr.12"
        om = Om(id, nume, adresa)
        bad_id = -23
        bad_nume = "ss"
        bad_adresa = "str. av nr. 11"
        bad_om = Om(bad_id, bad_nume, bad_adresa)
        validator = ValidatorPersoana()
        validator.valideaza_om(om)
        try:
            validator.valideaza_om(bad_om)
            assert False
        except Exception as ex:
            assert(str(ex)=="id invalid!\nnume invalid!\nadresa invalida!\n")

    def __test_add_om(self):
        id = 23
        nume = "Marius-Marcel"
        adresa = "str.av,nr.12"
        om = Om(id, nume, adresa)
        repo=OmRepository()
        repo.add_om(om)

        id = 23
        nume = "Alin-Andrei"
        adresa = "str.v,nr.1"
        om = Om(id, nume, adresa)
        repo = OmRepository()
        try:
            repo.add_om(om)
        except Exception as ex:
            assert(str(ex)=="id-ul exista deja!")

    def __test_add_file_and_get_all(self):
        repo = FileOmRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\persoane.txt")
        repo.golire()
        om = Om(12, "a-a", "str.1,nr.2")
        repo.add_om(om)
        assert repo.get_all()==[om]

    def __test_cdi_file(self):
        repo = FileOmRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\persoane.txt")
        repo.golire()
        om = Om(12, "a-a", "str.1,nr.2")
        repo.add_om(om)
        assert repo.cauta_id(12)==om

    def __test_get_all(self):
        id = 23
        nume = "Marius-Marcel"
        adresa = "str.av,nr.12"
        om = Om(id, nume, adresa)
        repo=OmRepository()
        repo.add_om(om)
        assert repo.get_all()==[om]

    def __test_stergere_om(self):
        id = 1
        nume = "Stfean-Vlad"
        adresa = ("str.1,nr.2")
        om = Om(id, nume, adresa)

        other_id = 2
        other_nume = "consola"
        other_adresa = "15/10/2025"
        other_om = Om(other_id, other_nume, other_adresa)
        repo = OmRepository()

        repo.add_om(om)
        repo.add_om(other_om)
        assert om in repo.get_all()
        assert other_om in repo.get_all()
        assert len(repo.get_all()) == 2
        repo.delete_om(id)
        assert other_om in repo.get_all()
        assert len(repo.get_all()) == 1

    def __test_file_stergere_om(self):
        id = 1
        nume = "Stfean-Vlad"
        adresa = ("str.1,nr.2")
        om = Om(id, nume, adresa)

        other_id = 2
        other_nume = "consola"
        other_adresa = "15/10/2025"
        other_om = Om(other_id, other_nume, other_adresa)

        repo = FileOmRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\persoane.txt")
        repo.golire()

        repo.add_om(om)
        repo.add_om(other_om)
        assert om in repo.get_all()
        assert other_om in repo.get_all()
        assert len(repo.get_all()) == 2
        repo.delete_om(id)
        assert other_om in repo.get_all()
        assert len(repo.get_all()) == 1


    def __test_modifica_persoana(self):
        id = 23
        nume = "Marius-Marcel"
        adresa = "str.av,nr.12"
        om = Om(id, nume, adresa)
        repo = OmRepository()
        repo.add_om(om)
        repo.modifica_om(om)

        id = 24
        nume = "MariusMarcel"
        adresa = "str.av,nr.12"
        om = Om(id, nume, adresa)
        repo = OmRepository()
        try:
            repo.add_om(om)
            repo.modifica_om(om)
        except Exception as ex:
            assert str(ex)=="nume invalid!\n"

    def __test_file_modifica_persoana(self):
        id = 23
        nume = "Marius-Marcel"
        adresa = "str.av,nr.12"
        om = Om(id, nume, adresa)
        repo = FileOmRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\persoane.txt")
        repo.golire()
        repo.add_om(om)
        om1=Om(id,"a-a","str.1,nr.2")
        repo.modifica_om(om1)
        assert repo.get_all()==[om1]

    def prun_teste(self):
        self.__test_create_om()
        self.__test_validate_om()
        self.__test_add_om()
        self.__test_get_all()
        self.__test_modifica_persoana()
        self.__test_stergere_om()
        self.__test_add_file_and_get_all()
        self.__test_file_modifica_persoana()
        self.__test_file_stergere_om()
        self.__test_cdi_file()