from .persoane import ConsolaPersoane
from .evenimente import ConsolaEvenimente
from .inscrieri import ConsolaInscrieri
from Exceptii import ValidError
from Exceptii import RepoError

class Consola:
    def __init__(self,consola_ev,consola_pers,consola_inscrieri):
        self.__consola_pers = consola_pers
        self.__consola_ev=consola_ev
        self.__consola_inscrieri=consola_inscrieri

    def run(self):
        while True:
            cmd = input(">>>")
            cmd = cmd.strip()
            if cmd == "exit":
                return
            parts = cmd.split(">")
            cmd_name = parts[0]
            if len(parts)>1:
                params = parts[1]
            else:
                params=[]
            if cmd_name in self.__consola_pers.comenzi:
                try:
                    self.__consola_pers.comenzi[cmd_name](params)
                except Exception as ex:
                    print(ex)
            elif cmd_name in self.__consola_ev.comenzi:
                try:
                    self.__consola_ev.comenzi[cmd_name](params)
                except ValueError as vae:
                    print(vae)
                except RepoError as re:
                    print("repo error\n")
                    print(re)
                except ValidError as ve:
                    print("validation error\n")
                    print(ve)
                except Exception as ex:
                    print("ui error\n")
                    print(ex)
            elif cmd_name in self.__consola_inscrieri.comenzi:
                try:
                    self.__consola_inscrieri.comenzi[cmd_name](params)
                except ValueError as vae:
                    print(vae)
                except RepoError as re:
                    print("repo error\n")
                    print(re)
                except ValidError as ve:
                    print("validation error\n")
                    print(ve)
                except Exception as ex:
                    print("ui error\n")
                    print(ex)
            else:
                print("Comanda nu este cunoscuta. Va rugam sa reincercati!")

        #            except ValueError as ve:
        # printf("UI Error",str(ve))
        # except exceptions.ValidationException as ve:
        #   printf("ValidationException", str(ve))
        # except exceptions.RepoException as re:
        #   printf("RepoException", str(re))

        #            except ValueError as ve:
        # printf("UI Error",str(ve))
        # except exceptions.ValidationException as ve:
        #   printf("ValidationException", str(ve))
        # except exceptions.RepoException as re:
        #   printf("RepoException", str(re))