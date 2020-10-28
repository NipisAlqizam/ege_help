import random

a = 'Сколько единиц содержится в двоичной записи значения выражения: {}'
subject = 1
theme = 1

def generate():
    a1 = random.randint(20,1000)
    a2 = random.randint(1,a1//2-1)
    problem = f'2^{a1}+4^{a2}-1'
    ans = bin(2**a1+4**a2-1).count('1')
    res = a.format(problem)
    return (res,ans)
