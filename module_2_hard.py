n = int(input('появляющееся число:'))
password = []
for i in range(1,n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            password.append(i)
            password.append(j)
        else: continue
print('пароль:', password)
