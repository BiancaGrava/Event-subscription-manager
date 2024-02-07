from Domain import Om
import random
class OmService:

    def __init__(self,repo_oameni,validator_oameni):
        self.__repo_oameni = repo_oameni
        self.__validator_oameni = validator_oameni

    def add_om(self,id_baller,name,value):
        '''
        adauga om in lista de oameni
        :param id_baller: id
        :param name: nume
        :param value: adresa
        :return:
        '''
        om = Om(id_baller,name,value)
        self.__validator_oameni.valideaza_om(om)
        self.__repo_oameni.add_om(om)

    def get_all_oameni(self):
        '''
        returneaza toata lista de oameni
        :return: lista completa de oameni
        '''
        return self.__repo_oameni.get_all()

    def delete_om(self,id):
        '''
        sterge din lista un om dupa id
        :param id:
        :return:
        '''
        return self.__repo_oameni.delete_om(id)

    def cauta_om(self,id):
        '''
        cauta in lista un om dupa id
        :param id: id
        :return: omul din lista, daca se afla in lista
        '''
        return self.__repo_oameni.cauta_id(id)

    def modifica_om(self, id, nume, adresa):
        '''
        modifica un om din lista
        :param id: id
        :param nume: nume
        :param adresa: adresa
        :return: lista de oameni cu omul cu id ul id modificat cu noile date
        '''
        om = Om(id, nume, adresa)
        self.__validator_oameni.valideaza_om(om)
        self.__repo_oameni.modifica_om(om)

    def genereaza_persoane(self,nr):
        g=0
        while g!=nr:
            new_id=random.randint(1,max(200,nr))
            list=["Stefan-Vlad","Bianca-Grava","Ana-Cosinzeana","Ana-Mara"]
            new_nume=random.choice(list)
            ladr=["str.1,nr.2","str.1,nr.3","str.1,nr.4","str.2,nr.1","str.2,nr.3","str.5,nr.1"]
            new_adresa=random.choice(ladr)
            new_om=Om(new_id,new_nume,new_adresa)
            try:
                self.__validator_oameni.valideaza_om(new_om)
                self.__repo_oameni.add_om(new_om)
                g+=1
            except:
                pass