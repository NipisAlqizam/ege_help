import random

t = 'При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 15 символов и содержащий только символы из 12-символьного набора: А, В, C, D, Е, F, G, H, К, L, M, N. В базе данных для хранения сведений о каждом пользователе отведено одинаковое и минимально возможное целое число байт. При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и минимально возможным количеством бит. Кроме собственно пароля, для каждого пользователя в системе хранятся дополнительные сведения, для чего отведено {} байт на одного пользователя.\nОпределите объём памяти (в байтах), необходимый для хранения сведений о {} пользователях. В ответе запишите только целое число — количество байт.'
subject = 1
theme = 2

def generate():
    a = random.randint(12,100)
    b = random.randint(3,10)*10
    ans = (8+a)*b
    return (t.format(a,b),ans)