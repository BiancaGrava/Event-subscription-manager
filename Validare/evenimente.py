from Exceptii import ValidError
class ValidatorEveniment:

    def valideaza_ev(self,ev):
        erori = ""

        id_ev1 = ev.get_id_ev()
        data1 = ev.get_data()
        timp1 = ev.get_timp()
        descriere1=ev.get_descriere()

        if id_ev1 < 0:
            erori += "id invalid!\n"

        d=0
        d1=data1.strip().split("/")
        try:
            d1[0]=int(d1[0])
        except ValueError:
            d=1
            erori+="introduceti data calendaristica in formatul zi/luna/an\n"

        if d==0:
            try:
                d1[1] = int(d1[1])
            except ValueError:
                d = 1
                erori += "introduceti data calendaristica in formatul zi/luna/an\n"

        if d==0:
            try:
                d1[2] = int(d1[2])
            except ValueError:
                d = 1
                erori += "introduceti data calendaristica in formatul zi/luna/an\n"
        if d==0:
            if int(d1[2])<2023:
                erori+="eveniment incheiat!\n"
            elif d1[2]>2035:
                erori+="eveniment prea indepartat!\n"

            luna=int(d1[1])
            ziua=int(d1[0])
            if luna in [4,6,9,11]:
                if ziua<1 or ziua>30:
                    erori+="ziua incorecta!\n"
            elif luna in [1,3,5,7,8,10,12]:
                if ziua<1 or ziua>31:
                    erori += "ziua incorecta!\n"
            elif luna==2:
                if int(d1[2])%4==0:
                    if ziua<1 or ziua>29:
                        erori += "ziua incorecta!\n"
                else:
                    if ziua<1 or ziua>28:
                        erori += "ziua incorecta!\n"

            if luna not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                erori += "luna incorecta!\n"

        t = timp1.split(":")
        if len(t) != 2:
            erori += "formatul timpului invalid!\n"
        else:
            try:
                t1=int(t[0])
                t2=int(t[1])
                if t1<0:
                    erori+="numar de ore inexistent!\n"
                if t2<0 or t2>59:
                    erori+="numar de minute inexistent!\n"
            except ValueError:
                erori+="timpul nu este in formatul h:min!\n"

        if descriere1=="":
            erori += "descriere invalida!\n"

        if len(erori) > 0:
            raise ValidError(erori)