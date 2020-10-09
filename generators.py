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

generate_inf = [generate_1, generate_2]
