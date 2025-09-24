#!/usr/bin/env python3

"""
- O programa recebe a quantidade de água disponível e a distância até o oásis,
e informa se a água é suficiente.
- Ian Fontanive
"""

agua = int(input("Quanto de água lhe resta, explorador? "))
dis =  int(input("Qual a distância até o Oásis? "))

agua_necessaria = dis * 2

if agua >= agua_necessaria:
    print("Não se preocupe, recione sua água com cautela e você chegará ao Oásis!")

else:
    print("Você não chegará ao Oásis.")
