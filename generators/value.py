import random

t = 'Вычислите массу кислорода, необходимого для полного сжигания {} л (н. у.) сероводорода. Ответ дайте в граммах с точностью до десятых.'
subject = 2
theme = 4

def generate():
    a = round(random.randint(1,20)/10,1)
    n = round(a*22.4, 3)
    ans = round(a*3*16, 3)
    return (t.format(n), ans)