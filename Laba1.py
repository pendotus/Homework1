# -*- coding: cp1251 -*-

name = "Mark"
print (name)

age = 18

print ("Меня зовут", name, ". Мне", age, "лет.")

name2 = "Марк" + "Марк" + "Марк" + "Марк" + "Марк"
print (name2)
print (name * 5)

age2 = int(input("Сколько тебе лет?"))
while age2>150 or age2<0:
    age2=int(input("Введите корректный возраст"))
YourName = input("Как тебя зовут?")

while YourName.isspace() == True:
    YourName = input("Введите корректное имя(без пробелов)")

while True:
    if YourName.isspace()== True:
        YourName = input("Введите корректное имя(без пробелов)")
    else:
        break


print ("Привет,", YourName)


if age2 < 10:
    print ("Да ты еще ребенок!")
elif age2 < 18:
    print ("Да ты еще школьник")
else:
    print ("Здарова дед")

i = YourName.count("")
i=i-2

b=i
while i > -1:
    if b == i:
        print (" ")
    elif i<b and i>0:
        print (YourName[i])
    else:
        print (" ")
    i -= 1

i=0
while i < 5:
    print (YourName[i])
    i += 1

i =YourName.count("") - 1
print ("Длина имени пользователя:", i)

YourName2 = YourName.upper()
print (YourName2)

YourName2 = YourName.lower()
print (YourName2)

YourName2 = YourName.swapcase()
print (YourName2)

YourName2 = YourName.swapcase()
print (YourName2)

answer = input("Сколько будет 2+2*2?")
while True:
    if answer == 6:
        print("Молодец!")
        break
    else:
        answer = input("Не правильно, попробуй еще раз!")