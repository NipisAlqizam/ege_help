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
    return generators

def generate(subject_name, theme_name):
    l = []
    for g in generators:
        if g.subject_name == subject_name and g.theme_name == theme_name:
            l.append(g)
    return random.choice(l).generate()

generators = get_generators()
