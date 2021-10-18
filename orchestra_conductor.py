class OrchestraConductor:
    def __init__(self, id_orchestra, id_conductor):
        self.__id_orchestra = id_orchestra
        self.__id_conductor = id_conductor

    def get_id_conductor(self):
        return self.__id_conductor