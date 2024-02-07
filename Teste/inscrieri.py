from Controller import InscrieriService
from Repository import FileInsRepo
from Repository import FileEvRepo
from Repository import FileOmRepo
from Domain import Evenimente
from Domain import Inscrieri
from Domain import Om
from Domain import EvenimentInscriere
from Validare import InscriereValidator
class TesteInscrieri:

    def __test_add(self):
        repo = FileInsRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\inscrieri.txt")
        repo.golire()
        om = Om(12, "a-a", "str.1,nr.2")
        om0 = Om(13, "b-a", "str.0,nr.1")
        ev1 = Evenimente(300, "12/03/2024", "12:00", "majorat")
        ev2 = Evenimente(301, "12/03/2024", "12:00", "majorat")
        ins1 = Inscrieri(om, ev1, 2)
        ins2 = Inscrieri(om, ev2, 3)
        ins3 = Inscrieri(om0, ev1, 5)
        repo.add_ins(ins1)
        assert repo.get_all() == [ins1]
        repo.add_ins(ins2)
        assert repo.get_all() == [ins1, ins2]
        repo.add_ins(ins3)

    def __test_perscmactv(self):
        repo = FileInsRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\inscrieri.txt")
        repop=FileOmRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\persoane.txt")
        repoe=FileEvRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\evenimente.txt")
        repo.golire()
        repop.golire()
        repoe.golire()
        val=InscriereValidator()
        serv=InscrieriService(repoe,repop,repo,val)
        om = Om(12, "a-a", "str.1,nr.2")
        om0 = Om(13, "b-a", "str.0,nr.1")
        ev1 = Evenimente(300, "12/03/2024", "12:00", "majorat")
        ev2 = Evenimente(301, "12/03/2024", "12:00", "majorat")
        repop.add_om(om)
        repop.add_om(om0)
        repoe.add_event(ev1)
        repoe.add_event(ev2)
        serv.inscriere_la_ev(12,300,1)
        serv.inscriere_la_ev(12,301,2)
        serv.inscriere_la_ev(13,300,5)
        assert serv.raport_persoane()==[om]

    def __test_print_and_subscribe(self):
        repo = FileInsRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\inscrieri.txt")
        repop = FileOmRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\persoane.txt")
        repoe = FileEvRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\evenimente.txt")
        repo.golire()
        repop.golire()
        repoe.golire()
        val = InscriereValidator()
        serv = InscrieriService(repoe, repop, repo, val)
        om = Om(12, "a-a", "str.1,nr.2")
        om0 = Om(13, "b-a", "str.0,nr.1")
        ev1 = Evenimente(300, "12/03/2024", "12:00", "majorat")
        ev2 = Evenimente(301, "12/03/2024", "12:00", "majorat")
        repop.add_om(om)
        repop.add_om(om0)
        repoe.add_event(ev1)
        repoe.add_event(ev2)
        serv.inscriere_la_ev(12, 300, 1)
        serv.inscriere_la_ev(12, 301, 2)
        serv.inscriere_la_ev(13, 300, 5)
        ins1 = EvenimentInscriere(12,300,"majorat","12/03/2024", 1)
        ins2 = EvenimentInscriere(12, 301,"majorat","12/03/2024",2)
        ins3 = EvenimentInscriere(13, 300,"majorat","12/03/2024",5)
        assert len(serv.print_all())==3
        #[ins1,ins2,ins3]

    def __test_listEv(self):
        repo = FileInsRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\inscrieri.txt")
        repop = FileOmRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\persoane.txt")
        repoe = FileEvRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\evenimente.txt")
        repo.golire()
        repop.golire()
        repoe.golire()
        val = InscriereValidator()
        serv = InscrieriService(repoe, repop, repo, val)
        om = Om(12, "a-a", "str.1,nr.2")
        om0 = Om(13, "b-a", "str.0,nr.1")
        ev1 = Evenimente(300, "12/03/2024", "12:00", "majorat")
        ev2 = Evenimente(301, "12/03/2024", "12:00", "majorat")
        repop.add_om(om)
        repop.add_om(om0)
        repoe.add_event(ev1)
        repoe.add_event(ev2)
        serv.inscriere_la_ev(12, 300, 1)
        ins1 = EvenimentInscriere(12, 300, "majorat", "12/03/2024", 1)
        assert len(serv.listEvents_om(12))==1#[ins1]
        ins2 = EvenimentInscriere(12, 301,"majorat","12/03/2024",2)
        serv.inscriere_la_ev(12, 301, 1)
        ins3 = EvenimentInscriere(13, 300,"majorat","12/03/2024",5)
        ins3 = EvenimentInscriere(13, 300,"majorat","12/03/2024",5)
        assert len(serv.listEvents_om(12))==2

    def __test_raport_ev_max(self):
        repo = FileInsRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\inscrieri.txt")
        repop = FileOmRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\persoane.txt")
        repoe = FileEvRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Teste\\evenimente.txt")
        repo.golire()
        repop.golire()
        repoe.golire()
        val = InscriereValidator()
        serv = InscrieriService(repoe, repop, repo, val)
        om = Om(12, "a-a", "str.1,nr.2")
        om0 = Om(13, "b-a", "str.0,nr.1")
        ev1 = Evenimente(300, "12/03/2024", "12:00", "majorat")
        ev2 = Evenimente(301, "12/03/2024", "12:00", "majorat")
        ev3=Evenimente(401, "12/03/2024", "12:00", "majorat")
        repop.add_om(om)
        repop.add_om(om0)
        repoe.add_event(ev1)
        repoe.add_event(ev2)
        repoe.add_event(ev3)
        serv.inscriere_la_ev(12, 300, 1)
        serv.inscriere_la_ev(12, 301, 2)
        serv.inscriere_la_ev(13, 300, 5)
        serv.inscriere_la_ev(13, 401, 5)
        serv.inscriere_la_ev(12, 401, 2)
        assert len(serv.raport_eveniment_maxim())==1

    def irun_teste(self):
        self.__test_add()
        self.__test_perscmactv()
        self.__test_print_and_subscribe()
        self.__test_listEv()
        self.__test_raport_ev_max()
