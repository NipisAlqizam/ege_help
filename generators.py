import db
import random

def generate_1():
    a = db.get_template(1)
    a1 = random.randint(20,1000)
    a2 = random.randint(1,a1//2-1)
    problem = f'2^{a1}+4^{a2}-1'
    ans = bin(2**a1+4**a2-1).count('1')
    a = a.format(problem)
    return (a,ans)

def generate_2():
    a = db.get_template(2)
    print()
    print(a)
    print()
    basis = random.choice([3,7])
    problem = [random.randint(1,20) for i in range(random.randint(1,4))]
    ps = '+'.join(map(str,problem))
    digit = random.randint(0,basis-1)
    
    ans = 0
    tmp = sum(problem)
    while tmp != 0:
        if tmp%basis == digit:
            ans += 1
        tmp //= basis
    a = a.format(ps, basis,digit)
    return (a,ans)

def generate_3():
    t = db.get_template(3)
    a = random.randint(12,100)
    b = random.randint(3,10)*10
    ans = (8+a)*b
    return (t.format(a,b),ans)

def generate_4():
    t = db.get_template(4)
    tmp = [[['один','четыре'], 
'''1. Na
2. K
3. Si
4. Mg
5. C''', ['12','35']]]
    a = random.randint(0,1)
    b = tmp[0][1]
    return (t.format(tmp[0][0][a],b), tmp[0][2][a])

def generate_5():
    t = db.get_template(5)
    a = round(random.randint(1,20)/10,1)
    n = a*22.4
    ans = a*3*16
    return (t.format(n), ans)

generate_inf = [[generate_1, generate_2],[generate_3]]
generate_chem = [[generate_4], [generate_5]]

def generate(subject_id, theme_id):
    print(theme_id)
    if subject_id == 0:
        l = len(generate_inf[theme_id])
        return generate_inf[theme_id][random.randint(0,l-1)]()
    elif subject_id == 1:
        l = len(generate_chem[theme_id])
        return generate_chem[theme_id][random.randint(0,l-1)]()
    else:
        return('', 0)
