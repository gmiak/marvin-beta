#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""funktioner för ryggsäck"""


def readinfo():
    """read file"""
    fhand = open('inv.data', 'r')
    data = fhand.read()
    count = len(open('inv.data').readlines())

    print('Ryggsäcken')
    print("===================" + "\n")
    print("Det finns %s blommor i ryggsäcken " %count)
    print('\n' + data + '\n')


def pick(pickflower):
    """pick a flower"""
    flowerList = list()
    flowerList.append(pickflower)
    count = len(open('inv.data').readlines())
    for eachitem in flowerList:
        fhand = open('inv.data', 'a')
        if count < 4:
            fhand.write(str(eachitem)+'\n')
            fhand.close()
            print("E-G tog upp %s " %pickflower)
        else:
            print("Ryggsäcken är full! E-G kan ej bära mer gejer!")

def drop(dropflower):
    """drop a flower"""
    fhand = open("inv.data", "r")
    lines = fhand.readlines()
    fhand.close()
    fhand = open('inv.data', 'w')
    for line in lines:
        if line != dropflower + "\n":
            fhand.write(line)
    fhand.close()
    print("E-G släppte %s " %dropflower)

def dropAll(files):
    """drop all flower"""
    with open(files, 'w'):
        pass
    print("E-G har släppt alla blommor!")
