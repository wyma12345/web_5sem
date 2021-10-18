from conductor import Conductor
from orchestra import Orchestra
from controlDB import ControlDB


def main():
    names_conductor = ['Константин', 'Евгений', 'Михаил', 'Илья']

    bd = ControlDB()
    # Создаем дирижеров
    bd.set_conductors(*names_conductor)

    # Добавляем оркестры к дирижерам
    bd.set_orchestra("ансамбль Константина - 1", 7, 0)
    bd.set_orchestra("ансамбль Константина - 2", 16, 0)
    bd.set_orchestra("ансамбль Константина - 3", 5, 0)
    bd.set_orchestra("ансамбль Евгения - 1", 24, 1)
    bd.set_orchestra("ансамбль Евгения - 2", 12, 1)
    bd.set_orchestra("ансамбль Михаила - 1", 17, 2)
    bd.set_orchestra("ансамбль Ильи - 1", 4, 3)
    bd.set_orchestra("ансамбль Ильи - 2", 28, 3)

    print(bd.getSort())#Задание 1
    print(bd.get_cost())#Задание 2

    # для М-М
    bd.set_many_orchestra("ан К,И - 1", 7, 0, 3)
    bd.set_many_orchestra("ан К,Е - 2", 16, 0, 1)
    bd.set_many_orchestra("гн К,М - 3", 5, 0, 2)
    bd.set_many_orchestra("ан Е,М - 1", 24, 1, 2)
    bd.set_many_orchestra("гн Е,И - 2", 12, 1, 3)
    bd.set_many_orchestra("гн М,И - 1", 17, 2, 3)

    print(bd.get_orcetst_cond())#Задание 3


if __name__ == '__main__':
    main()
