class ValidatorPersoana:

    def valideaza_om(self,om):
        erori = ""

        nume1 = om.get_nume()
        adresa1 = om.get_adresa()
        id1 = om.get_id()
        erori = ""
        if id1 < 0:
            erori += "id invalid!\n"

        l = nume1.split("-")
        if len(l) < 2:
            erori += "nume invalid!\n"

        d = adresa1.split(",")
        if len(d) != 2:
            erori += "adresa invalida!\n"
        else:
            strd = d[0].split(".")
            nr = d[1].split(".")
            if strd[0].strip() != "str":
                erori += "adresa invalida!\n"
            elif nr[0].strip() != "nr":
                erori += "adresa invalida!\n"
            try:
                n = int(nr[1].strip())
            except ValueError:
                erori += "adresa invalida!\n"

        if len(erori) > 0:
            raise Exception(erori)