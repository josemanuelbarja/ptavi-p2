#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

calcu = calcoo.Calculadora


class CalculadoraHija(calcu):
    def mult(self, op1, op2):
        return op1 * op2

    def div(self, op1, op2):
        return op1 / op2

if __name__ == "__main__":
    calcuhija = CalculadoraHija()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    if sys.argv[2] == "suma":
        result = calcuhija.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calcuhija.minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = calcuhija.mult(operando1, operando2)
    elif sys.argv[2] == "divide":
        try:
            result = calcuhija.div(operando1, operando2)
        except ZeroDivisionError:
            sys.exit("Error: Division by zero is not allowed")
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')
    print(result)
