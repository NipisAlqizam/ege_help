import importlib
from generate import generators
def get_subjects():
    l = set()
    for g in generators:
        l.add(g.subject_name)
    return sorted(list(l))

def get_themes(subject_name):
    l = set()
    for g in generators:
        if g.subject_name == subject_name:
            l.add(g.theme_name)
    return sorted(list(l))

