import csv
import random
import os


def generate_random_with_step(start, end, step):
    value=random.randrange(start,end,step)
    return value

START_p: int = 4000
END_p: int = 11000
STEP_p: int = 5

START_f: int = 235
END_f: int = 240
STEP_f: int = 1

epohs: int= 1000000
for i in range(epohs):
    value1 = generate_random_with_step(START_p, END_p, STEP_f)
    value2 = generate_random_with_step(START_f, END_f, STEP_f)
    list1: list = [value1, value2 ]
    if list1[0]<=5000 and list1[1]>=237:
        list1.append(0)
    if list1[0]<=5000 or list1[1]<=237:
        list1.append(1)
    elif list1[0]>5000 and list1[0]<10000 or list1[1]<237:
        list1.append(1)
    elif list1[0]>=10000 or list1[1]<237:
        list1.append(2)
    if len(list1) > 3:
        list1.pop(3)

    filename = "../data.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Value1", "Value2", "Empty"])

        writer.writerow(list1)

    print(f"Данные добавлены в файл {filename}")
    print(f"Сгенерированные значения: {value1}, {value2}")
