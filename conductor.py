class Conductor:
    def __init__(self, name):
        self.__id_conductor = id(self)
        self.__name = name
        self.n = 0

    def __repr__(self):
        return self.__name

    def return_id(self):
        return self.__id_conductor

    def up_n(self) -> None:
        self.n += 1

    def get_n(self) -> int:
        return self.n
