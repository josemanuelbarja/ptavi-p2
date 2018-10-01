#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

lines = 0  # 'inicializo lineas'
cont_op = 1  # 'inicializo contador de operaciones'

with open(sys.argv[1], 'r') as fichcsv:
    fich = csv.reader(fichcsv, delimiter=",")
    lineas = list(fich)

for palabras in lineas:
    operaciones = palabras[2:]
    if __name__ == "__main__":
        calcuhija = calcoohija.CalculadoraHija()
        result = 0
        try:
            if palabras[0] == "suma":
                result = int(palabras[1])
                for operando in operaciones:
                    cont_op += 1
                    operando1 = int(palabras[cont_op])
                    result = calcuhija.plus(result, operando1)
                print(result)
            elif palabras[0] == "resta":
                result = int(palabras[1])
                for operando in operaciones:
                    cont_op += 1
                    operando1 = int(palabras[cont_op])
                    result = calcuhija.minus(result, operando1)
                print(result)
            elif palabras[0] == "divide":
                result = int(palabras[1])
                for operando in operaciones:
                    cont_op += 1
                    operando1 = int(palabras[cont_op])
                    try:
                        result = calcuhija.div(result, operando1)
                    except ZeroDivisionError:
                        sys.exit("Error: Division by zero is not allowed")
                print(result)
            elif palabras[0] == "multiplica":
                result = int(palabras[1])
                for operando in operaciones:
                    cont_op += 1
                    operando1 = int(palabras[cont_op])
                    result = calcuhija.mult(result, operando1)
                print(result)
            else:
                sys.exit('Operación inválida.')
        except ValueError:
            sys.exit("Error: Non numerical parameters")
        cont_op = 1  # 'inicializo a 1 para la siguiente linea'
