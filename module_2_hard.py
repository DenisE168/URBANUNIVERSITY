import random
def get_cipher():
    numbers = list(range(3, 21))
    cipher = random.choice(numbers)
    return cipher
n = get_cipher()
print('Шифр   :', n)
n2 = int(input('Введите шифр : '))
while n != n2:
  print("Шифр неверный")
  n2 = int(input("Введите шифр : "))
ans =""
for a in range(1, n2):
    for b in range(a+1,n2):
        if n % (a + b) == 0:
            ans +=f"{a}{b}"
print("Пароль : ",ans )

