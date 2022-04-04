import json
import pandas as pd
import os
from colorama import *
from collections import OrderedDict


def guardarestadisticas(nombre, partida):
    filename = "partidas_guardadas.json"
    new_data = OrderedDict({nombre: partida})
    new_data.update(json.load(open(filename), object_pairs_hook=OrderedDict))
    json.dump(new_data, open(filename, "w"))

    with open(filename, 'r') as file:
        dic = json.load(file)
        dic2 = {}
        for key in dic:
            if key == nombre:
                dic2[nombre] = partida
            else:
                dic2[key] = dic[key]

    with open(filename, 'w') as file:
        json.dump(dic2, file)

guardarestadisticas("A", [["_" for _ in range(9)] for _ in range(9)])

guardarestadisticas("B", [["_" for _ in range(9)] for _ in range(9)])
