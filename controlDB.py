from conductor import Conductor
from orchestra import Orchestra

class ControlDB:
    def __init__(self):
        self.list_conductors = []
        self.list_orchestra = []

    def getSort(self) -> list:
        return sorted(self.list_orchestra, key=lambda x: x.get_name())  # сортируем

    def get_cost(self) -> list:
        return list(map(lambda x: '{} - кол-ом {}'.format(x,x.get_n()),sorted(self.list_conductors, key=lambda x: x.get_n())))  # сортируем

    def get_orcetst_cond(self):
        l = []
        for i in self.list_orchestra:
            if len(i.get_id_conductor()) > 1 and i.get_name()[:2]=='ан':
                sr = 'Оркестр: {} дирижеры: '.format(i.get_name())
                for j in i.get_id_conductor():
                    sr += str(j.get_id_conductor()) + '; '
                l.append(sr)
        return l



    def set_conductors(self,*arg):
        for i in arg:
            self.list_conductors.append(Conductor(i))

    def set_orchestra(self, name:str, size:int, id_cond:int):
        self.list_orchestra.append(Orchestra(name, size, [self.list_conductors[id_cond]]))
        self.list_conductors[id_cond].up_n()

    def set_many_orchestra(self, name:str, size:int, *id_cond:int):
        self.list_orchestra.append(Orchestra(name, size, [self.list_conductors[x] for x in id_cond]))