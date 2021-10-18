from  orchestra_conductor import OrchestraConductor

class Orchestra:
    def __init__(self, name, size, id_conductor:list):
        #global num_orchestra
        #self.__id_orchestra = num_orchestra
        self.__id_orchestra = id(self)
        self.__name = name
        self.__size = size
        if len(id_conductor) == 1:
            self.__id_conductor = id_conductor
        elif len(id_conductor) > 1:
            self.__id_conductor = []
            for i in id_conductor:
                self.__id_conductor.append(OrchestraConductor(self.__id_orchestra, i))

        #num_orchestra += 1

    def get_name(self):
        return self.__name

    def get_id_conductor(self):
        return self.__id_conductor

    def __repr__(self):
        return 'название: {}, дирижер: {}'.format(self.__name, self.__id_conductor)
