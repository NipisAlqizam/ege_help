import random

t = 'Определите, атомы каких двух из указанных в ряду элементов имеют на внешнем энергетическом уровне {} электрона.\n{}'
subject = 2
theme = 3

def generate():
    tmp = [[['один','четыре'], 
'''1. Na
2. K
3. Si
4. Mg
5. C''', ['12','35']]]
    a = random.randint(0,1)
    b = tmp[0][1]
    return (t.format(tmp[0][0][a],b), tmp[0][2][a])