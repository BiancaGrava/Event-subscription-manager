from Validare import ValidatorPersoana
from UI import ConsolaPersoane
from Repository import OmRepository
from Repository import FileOmRepo
from Controller import OmService
from Teste import TestePersoane

from Validare import ValidatorEveniment
from UI import ConsolaEvenimente
from Repository import EventRepository
from Repository import FileEvRepo
from Controller import EvService

from UI import Consola
from Teste import TesteEvenimente

from Validare import InscriereValidator
from UI import ConsolaInscrieri
from Repository import InscrieriRepo
from Repository import FileInsRepo
from Controller import InscrieriService
from Teste import TesteInscrieri

def main():
    """fara fisier"""
    """p=TestePersoane()
    p.prun_teste()
    e=TesteEvenimente()
    e.erun_teste()
    i=TesteInscrieri()
    i.irun_teste()
    repo = OmRepository()
    validator = ValidatorPersoana()
    service = OmService(repo,validator)
    console = ConsolaPersoane(service)

    repoe = EventRepository()
    validatore = ValidatorEveniment()
    servicee = EvService(repoe, validatore)
    consolee = ConsolaEvenimente(servicee)

    repoi=InscrieriRepo()
    validatori=InscriereValidator
    servicei=InscrieriService(repoe,repo,repoi,validatori)
    consolei=ConsolaInscrieri(servicei)

    cons=Consola(consolee,console,consolei)
    cons.run()"""

    """cu fisier"""

    p = TestePersoane()
    p.prun_teste()
    e = TesteEvenimente()
    e.erun_teste()
    i=TesteInscrieri()
    i.irun_teste()
    repo = FileOmRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Repository\\persoane.txt")
    validator = ValidatorPersoana()
    service = OmService(repo, validator)
    console = ConsolaPersoane(service)

    repoe = FileEvRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Repository\\evenimente.txt")
    validatore = ValidatorEveniment()
    servicee = EvService(repoe, validatore)
    consolee = ConsolaEvenimente(servicee)

    repoi = FileInsRepo("D:\\trimestrul 4 2023\\UBB\\lab9_final1\\Repository\\inscriere.txt")
    validatori = InscriereValidator
    servicei = InscrieriService(repoe, repo, repoi, validatori)
    consolei = ConsolaInscrieri(servicei)

    cons = Consola(consolee, console, consolei)
    cons.run()

main()

