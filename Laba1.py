# -*- coding: cp1251 -*-

name = "Mark"
print (name)

age = 18

print ("���� �����", name, ". ���", age, "���.")

name2 = "����" + "����" + "����" + "����" + "����"
print (name2)
print (name * 5)

age2 = int(input("������� ���� ���?"))
while age2>150 or age2<0:
    age2=int(input("������� ���������� �������"))
YourName = input("��� ���� �����?")

while YourName.isspace() == True:
    YourName = input("������� ���������� ���(��� ��������)")

while True:
    if YourName.isspace()== True:
        YourName = input("������� ���������� ���(��� ��������)")
    else:
        break


print ("������,", YourName)


if age2 < 10:
    print ("�� �� ��� �������!")
elif age2 < 18:
    print ("�� �� ��� ��������")
else:
    print ("������� ���")

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
print ("����� ����� ������������:", i)

YourName2 = YourName.upper()
print (YourName2)

YourName2 = YourName.lower()
print (YourName2)

YourName2 = YourName.swapcase()
print (YourName2)

YourName2 = YourName.swapcase()
print (YourName2)

answer = input("������� ����� 2+2*2?")
while True:
    if answer == 6:
        print("�������!")
        break
    else:
        answer = input("�� ���������, �������� ��� ���!")