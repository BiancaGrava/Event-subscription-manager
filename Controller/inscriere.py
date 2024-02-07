#rapoarte
#lista=repoinscr.getall()
from Domain import Inscrieri
from Domain import EvenimentInscriere
from Domain import Om
from Domain import Evenimente

from Repository import FileEvRepo
from Repository import FileOmRepo
from Repository import  FileInsRepo

from Validare import InscriereValidator

def maxim(a,b):
    if a>b:
        return a
    else: return b

class InscrieriService:
    def __init__(self,repo_ev,repo_om,repo_ins,validator_ins):
        self.__repo_ev=repo_ev
        self.__repo_om=repo_om
        self.__repo_ins=repo_ins
        self.__validator_ins=validator_ins

    def inscriere_la_ev(self,id_om,id_ev,nrp):
        #lista = self.__repo_ins.cautare_dupa_id(id_om,id_ev)
        #if lista is not None:
        #    raise Exception("pers inscrisa")
        try:
            om=self.__repo_om.cauta_id(id_om)
            eveniment=self.__repo_ev.cauta_id_ev(id_ev)
            insc=self.__repo_ins.cautare_dupa_id(id_om,id_ev)
            if insc!=None:
                raise Exception("inscrierea exista!")
            else:
                ins=Inscrieri(om,eveniment,nrp)
                self.__repo_ins.add_ins(ins)
        except Exception as ex:
            raise Exception(ex)
        #return ins
    def listEvents_om(self,id_om):#complexitate = O(n)
        try:
            persoana=self.__repo_om.cauta_id(id_om)
            inscrierile = self.__repo_ins.get_all()
            lista_ceruta = []
            for inscriere in inscrierile:
                if inscriere.get_persoana().get_id() == id_om:
                    x1 = inscriere.get_persoana().get_id()
                    x2 = inscriere.get_ev().get_id_ev()
                    x3 = inscriere.get_ev().get_descriere()
                    x4 = inscriere.get_ev().get_data()
                    x5 = inscriere.get_nrp()
                    a = EvenimentInscriere(x1, x2, x3, x4, x5)
                    lista_ceruta.append(a)
            lista_ceruta = sorted(lista_ceruta, key=lambda x: (x.getDescriere(), x.getData(), x.getPers()),reverse=False)
            return lista_ceruta
        except Exception as ex:
            raise Exception(ex)

    def calc_max(self,lista_om,lista_ins):
        if lista_om==[]:
            return 0
        else:
            nrc=0
            for insc in lista_ins:
                if insc.get_persoana()==lista_om[0]:
                    nrc+=1
            return maxim(nrc,self.calc_max(lista_om[1:],lista_ins))


    def raport_persoane(self):
        inscrierile=self.__repo_ins.get_all()
        oamenii=self.__repo_om.get_all()
        maxim=self.calc_max(oamenii,inscrierile)
        lista_ceruta=[]
        for om in oamenii:
            nrc=0
            for inscriere in inscrierile:
                if inscriere.get_persoana()==om :
                    nrc+=1
            if nrc==maxim:
                lista_ceruta.append(om)
        return lista_ceruta

    def sortare_nrp(self,lista):
        lista_sortata=sorted(lista,key=lambda x: (x.getPers(),x.getDescriere()),reverse=False)
        return lista_sortata


    def raport_eveniment_maxim(self):
        nrt=0
        lista_ceruta = []
        events=self.__repo_ev.get_all()
        inscrierile = self.__repo_ins.get_all()
        x=0
        for event in events:
            nrt+=1
            nrc=0
            for inscriere in inscrierile:
                if inscriere.get_ev()==event:
                    nrc+=inscriere.get_nrp()
            x+=1
            ev=EvenimentInscriere(x,event.get_id_ev(),event.get_descriere(),event.get_data(),nrc)
            lista_ceruta.append(ev)
        events=lista_ceruta[0:]
        """for i in range(0,nrt+1):
            for j in range(i,nrt):
                if events[i].getPers()<events[j].getPers():
                    a=i
                    b=j
                    om=events[i]
                    events[i]=events[j]
                    events[j]=om
                    i=a
                    j=b"""
        #bubblesort
        events=bubblesort(events,nrt)
        nrt=nrt//5
        lista=[]
        for i in range(nrt+1):
            lista.append(events[i])
        return lista

    def raport_eveniment_minim(self):
        nrt=0
        lista_ceruta = []
        events=self.__repo_ev.get_all()
        inscrierile = self.__repo_ins.get_all()
        x=0
        for event in events:
            nrt+=1
            nrc=0
            for inscriere in inscrierile:
                if inscriere.get_ev()==event:
                    nrc+=inscriere.get_nrp()
            x+=1
            ev=EvenimentInscriere(x,event.get_id_ev(),event.get_descriere(),event.get_data(),nrc)
            lista_ceruta.append(ev)
        events=lista_ceruta[0:]
        events=bubblesort2(events,nrt)
        if len(events)>=5:
            lista=[]
            lista.append(events[0])
            lista.append(events[1])
            lista.append(events[2])
            lista.append(events[3])
            lista.append(events[4])
            return lista
        else:
            raise Exception("lista nu are 5 inscrieri")

    def print_all(self):
        lista = self.__repo_ins.get_all()
        lista_ceruta=[]
        for inscriere in lista:
            ev = EvenimentInscriere(inscriere.get_persoana().get_id(), inscriere.get_ev().get_id_ev(), inscriere.get_ev().get_descriere(), inscriere.get_ev().get_data(), inscriere.get_nrp())
            lista_ceruta.append(ev)
        return lista_ceruta

def bubblesort(events, nrt):
    for i in range(nrt + 1):
        for j in range(0, nrt - i - 1):
            if events[j].getPers() < events[j + 1].getPers():
                events[j], events[j + 1] = events[j + 1], events[j]
    return events

def bubblesort2(events, nrt):
    for i in range(nrt + 1):
        for j in range(0, nrt - i - 1):
            if events[j].getPers() > events[j + 1].getPers():
                events[j], events[j + 1] = events[j + 1], events[j]
    return events