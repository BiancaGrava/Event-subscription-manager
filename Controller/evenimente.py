from Domain import Evenimente
import random
class EvService:

    def __init__(self,repo_ev,validator_ev):
        self.__repo_ev = repo_ev
        self.__validator_ev = validator_ev

    def add_ev(self,id_ev,data,timp,descriere):
        '''
                adauga eveniment in lista de evenimente
                :param id_ev: id
                :param data: data
                :param timp: timp
                :param descriere: descriere
                :return:
                '''
        ev = Evenimente(id_ev,data,timp,descriere)
        self.__validator_ev.valideaza_ev(ev)
        self.__repo_ev.add_event(ev)

    def get_all_evenimente(self):
        return self.__repo_ev.get_all()
    def delete_ev(self,id):
        return self.__repo_ev.delete_ev(id)
    def modifica_ev(self, id, data, timp,descriere):
        ev = Evenimente(id, data, timp,descriere)
        self.__validator_ev.valideaza_ev(ev)
        self.__repo_ev.modifica_ev(ev)

    def cauta_ev(self,id):
        return self.__repo_ev.cauta_id_ev(id)

    def genereaza_evenimente(self,nr):
        g=0
        while g!=nr:
            new_id=random.randint(1,max(200,nr))
            list=["12/05/2023","13/04/2024","07/06/2023","08/09/2025"]
            new_data=random.choice(list)
            lora=["00:20","01:30","00:40","01:00","00:35"]
            new_ora=random.choice(lora)
            l=["eveniment1","va tine 2 zile","botez","nunta","majorat"]
            new_descriere=random.choice(l)
            new_om=Evenimente(new_id,new_data,new_ora,new_descriere)
            try:
                self.__validator_ev.valideaza_ev(new_om)
                self.__repo_ev.add_event(new_om)
                g+=1
            except:
                pass
            #generator -> gield