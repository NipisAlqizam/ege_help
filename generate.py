import os
import importlib
import db
import random

def get_generator_names():
    l = os.listdir('generators')
    generators = []
    for i in l:
        if i[-3:] == '.py':
            generators.append(i[:-3])
    return generators

def get_generators():
    names = get_generator_names()
    generators = [importlib.import_module('generators.'+name) for name in names]
    res = [[],[],[],[]]
    for g in generators:
        res[g.theme-1].append(g)
    return res

def generate(subject_id, theme_id):
    l = len(generators[theme_id])-1
    return generators[theme_id][random.randint(0,l)].generate()

generators = get_generators()