class ConsolaPersoane:

    def __init__(self,service_oameni):
        self.__service_oameni = service_oameni
        self.comenzi = {
            "adauga persoana":self.__ui_add_om,
            "afiseaza persoane":self.__ui_print_oameni,
            "modifica persoana":self.__ui_modifica_om,
            "sterge persoana": self.__ui_del_oameni,
            "cauta persoana": self.__ui_cauta_om,
            "genereaza oameni": self.__ui_aduga_oameni_random
        }
    def __ui_add_om(self,params):
        p=params.strip().split(" ")
        if len(p)!=3:
            print("nr parametrii invalid!")
            return
        try:
            id = int(p[0])
            nume = p[1]
            adresa = p[2]
        except ValueError:
            raise Exception("valoare numerica invalida!")
        self.__service_oameni.add_om(id,nume,adresa)
        print("persoana adaugata cu succes!")
    def __ui_print_oameni(self,params):
        if len(params)!=0:
            print("nr parametrii invalid!")
            return
        oameni = self.__service_oameni.get_all_oameni()
        for om in oameni:
            print(om)

    def __ui_del_oameni(self,params):
        p = params.strip().split(" ")
        if len(p) != 1:
            print("nr parametrii invalid!")
            return
        try:
            id = int(p[0])
            oameni = self.__service_oameni.delete_om(id)
            for om in oameni:
                print(om)
        except ValueError:
            print("id ul trebuie sa fie un numar intreg!")

    def __ui_cauta_om(self,params):
        p = params.strip().split(" ")
        if len(p) != 1:
            print("nr parametrii invalid!")
            return
        try:
            id = int(p[0])
            om = self.__service_oameni.cauta_om(id)
            print(om)
        except ValueError:
            print("id ul trebuie sa fie un numar intreg!")

    def __ui_modifica_om(self, params):
        p=params.strip().split(" ")
        if (len(p) != 3):
            print("nr parametrii invalid!")
            return
        try:
            id_student = int(p[0])
            nume = p[1]
            grup = p[2]
        except ValueError:
            raise Exception("valoare numerica invalida!")
        self.__service_oameni.modifica_om(id_student,nume,grup)
        print("persoana modificata cu succes!")

    def __ui_aduga_oameni_random(self,params):
        p = params.strip().split(" ")
        if (len(p) != 1):
            print("nr parametrii invalid!")
            return
        try:
            nr=int(p[0])
        except ValueError:
            raise Exception("valoare numerica invalida!")
        self.__service_oameni.genereaza_persoane(nr)
        print("persoane adaugate cu succes!")

