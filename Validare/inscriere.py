from Exceptii import ValidError
from Domain import Om
from Domain import Evenimente
from Domain import Inscrieri
class InscriereValidator:
    """
     Validator for grades
    """
    def validate(self,gr):
        """
         Validate grade
         gr Grade
         raise ValidateException if the grade is not between 0 and 10
        """
        if gr.get_nrp()<=0 or gr.get_nrp()>10:
            raise ValidError("Numarul de persoane inscrise la eveniment prin persoana data este minim 1 si maxim 10")

def testValidateInscrieri():
    om = Om(1, "Ion-Marcel", "str.Cluj,nr.3")
    ev = Evenimente(12,"12/03/2024","12:00","aa")
    ins=Inscrieri(om,ev,0)
    val = InscriereValidator()
    try:
        val.validate(ins)
        assert False
    except ValidError:
        assert True

testValidateInscrieri()