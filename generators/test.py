import random

t = 'Определите, атомы каких двух из указанных в ряду элементов имеют на внешнем энергетическом уровне {} электрона(ов).\n{}'
subject_name = "Химия"
theme_name = "Электронная конфигурация атома"
l = [['Li','Na','K','Rb','Cs'], ['Be', 'Mg', 'Ca', 'Sr', 'Ba'], ['B', 'Al','Ga', 'In', 'Tl'], ['C', 'Si', 'Ge', 'Sn', 'Pb'], ['N', 'P', 'As', 'Sb', 'Bi'], ['O', 'S', 'Se', 'Te'], ['F', 'Cl', 'Br', 'I']]


def generate():
    correct = random.randint(0,6)
    a = [correct, correct]
    for i in range(3):
        tmp = random.randint(0,6)
        while tmp == correct:
            tmp = random.randint(0,6)
        a.append(tmp)
    random.shuffle(a)
    ans = []
    for i,j in enumerate(a):
        if j == correct:
            ans.append(i+1)
    ans = ''.join(map(str,ans))
    b = [random.choice(l[i]) for i in a]
    test = '\n'.join([f'{i+1}. {j}' for i,j in enumerate(b)])
    return (t.format(correct+1, test), ans)
    

if __name__ == "__main__":
    print(generate()[0])