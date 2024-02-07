class ConsolaInscrieri:

    def __init__(self,service_ins):
        self.__service_ins = service_ins
        self.comenzi = {
            "inscrie persoana la eveniment":self.__ui_inscriere,
            "afiseaza toate inscrierile":self.__ui_print_ev,
            "persoana cea mai activa": self.__ui_persoana_cea_mai_activa,
            "evenimentele unui participant": self.__ui_listEvents_om,
            "evenimentele cele mai cautate": self.__ui_get_20_percent,
            "cele 5 evenimente cel mai putin cautate": self.__ui_last_5
            #practic,am pana la lab 10 cu tot cu modificare
            #mai am de facut testele cu Pyunit si sortarea cum cere lab12
            #functioneaza pentru date corecte
        }
    def __ui_inscriere(self,params):
        p=params.strip().split(" ")
        if len(p)!=3:
            print("nr parametrii invalid!")
            return
        try:
            id_om = int(p[0])
            id_ev = int(p[1])
            nrp = int(p[2])
        except ValueError:
            raise Exception("valoare numerica invalida!")
        self.__service_ins.inscriere_la_ev(id_om,id_ev,nrp)
        print("inscriere adaugata cu succes!")
    def __ui_print_ev(self,params):
        if len(params)!=0:
            print("nr parametrii invalid!")
            return
        inscrieri = self.__service_ins.print_all()
        for ins in inscrieri:
            print(ins)

    def __ui_listEvents_om(self,params):
        """evenimentele unui participant"""
        p = params.strip().split(" ")
        if len(p) != 1:
            print("nr parametrii invalid!")
            return
        try:
            id = int(p[0])
            evenimente = self.__service_ins.listEvents_om(id)
            for ev in evenimente:
                print(ev)
        except ValueError:
            raise Exception("id ul trebuie sa fie un numar intreg!")

    def __ui_get_20_percent(self, params):
        if len(params) != 0:
            print("nr parametrii invalid!")
            return
        lista_ev_cerute=self.__service_ins.raport_eveniment_maxim()
        for ev in lista_ev_cerute:
            print(str(ev))
            #print(" ")
            #print(ev.getPers())
            #print('\n')

    def __ui_persoana_cea_mai_activa(self, params):
        """persoana cea mai activa"""
        if len(params) != 0:
            print("nr parametrii invalid!")
            return
        persoanele=self.__service_ins.raport_persoane()
        for om in persoanele:
            print(om.get_nume()+" ; cu ID-ul: "+str(om.get_id()))


    def __ui_last_5(self,params):
        if (len(params) != 0):
            print("nr parametrii incorect!")
            return
        try:
            lista_ev_cerute = self.__service_ins.raport_eveniment_minim()
            for ev in lista_ev_cerute:
                print(str(ev))
        except Exception as ex:
            print(ex)
