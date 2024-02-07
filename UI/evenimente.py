class ConsolaEvenimente:

    def __init__(self, service_ev):
        self.__service_ev = service_ev
        self.comenzi = {
            "adauga eveniment": self.__ui_add_ev,
            "afiseaza evenimente": self.__ui_print_ev,
            "modifica eveniment": self.__ui_modifica_ev,
            "sterge eveniment": self.__ui_del_ev,
            "cauta eveniment": self.__ui_cauta_ev,
            "genereaza evenimente": self.__ui_aduga_evenimente_random
        }

    def __ui_add_ev(self, params):
        p = params.strip().split(" ")
        if len(p) != 4:
            raise Exception("nr parametrii invalid!")
        try:
            id_ev = int(p[0])
            nume = p[1]
            adresa = p[2]
            t = p[3]
        except ValueError:
            raise Exception("valoare numerica invalida!")
        self.__service_ev.add_ev(id_ev, nume, adresa, t)
        print("eveniment adaugat cu succes!")

    def __ui_print_ev(self, params):
        if len(params) != 0:
            raise Exception("nr parametrii invalid!")
        evenimente = self.__service_ev.get_all_evenimente()
        for ev in evenimente:
            print(ev)

    def __ui_del_ev(self, params):
        p = params.strip().split(" ")
        if len(p) != 1:
            raise Exception("nr parametrii invalid!")
        try:
            id_ev = int(p[0])
            evenimente = self.__service_ev.delete_ev(id_ev)
            for ev in evenimente:
                print(ev)
        except ValueError:
            raise Exception("id ul trebuie sa fie un numar intreg!")

    def __ui_cauta_ev(self, params):
        p = params.strip().split(" ")
        if len(p) != 1:
            raise Exception("nr parametrii invalid!")
        try:
            id_ev = int(p[0])
            ev = self.__service_ev.cauta_ev(id_ev)
            print(ev)
        except ValueError:
            raise Exception("id ul trebuie sa fie un numar intreg!")

    def __ui_modifica_ev(self, params):
        p = params.strip().split(" ")
        if len(p) != 4:
            raise Exception("nr parametrii invalid!")
        try:
            id_ev = int(p[0])
            data = p[1]
            timp = p[2]
            descriere = p[3]
        except ValueError:
            raise Exception("valoare numerica invalida!")
        self.__service_ev.modifica_ev(id_ev, data, timp, descriere)
        print("eveniment modificata cu succes!")

    def __ui_aduga_evenimente_random(self, params):
        p = params.strip().split(" ")
        if len(p) != 1:
            print("nr parametrii invalid!")
            return
        try:
            nr = int(p[0])
        except ValueError:
            raise Exception("valoare numerica invalida!")
        self.__service_ev.genereaza_evenimente(nr)
        print("evenimente adaugate cu succes!")
