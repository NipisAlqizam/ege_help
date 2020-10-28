import random

a = 'Значение арифметического выражения: {} – записали в системе счисления с основанием {}. Сколько цифр «{}» содержится в этой записи?'
subject = 1
theme = 1

def generate():
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
    res = a.format(ps, basis,digit)
    return (res,ans)