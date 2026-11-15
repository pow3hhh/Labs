#сведения о приеме 
priem = ("26.10.2026", 312, "Смирнова")

#список номеров карт 
zapis = [2104, 2121, 2140, 2158, 2173, 2190]

#множество номеров карт пациентов, пришедших на прием 
poseshchenie = {2104, 2140, 2158, 2190}

baza_pacientov = {
    2104: "Мария Марьевна",
    2121: "Алексей Алексеич",
    2140: "Иван Иванов",
    2158: "Елена Олеговна",
    2173: "Олег Олегович",
    2190: "Анна Соколова"
}

print(f"Прием: {priem[0]}, кабинет {priem[1]}, врач {priem[2]}")
print(f"Запись пациентов: {', '.join(map(str, zapis))}")
print(f"Пациенты, посетившие врача: {', '.join(map(str, poseshchenie))}")


#словарь
print("Пациенты:", end=" ")
pacienty_str = [f"{k} - {v}" for k, v in baza_pacientov.items()]
print("; ".join(pacienty_str))


novyi_pacient = 2207
zapis.append(novyi_pacient)
print(f"После добавления пациента: {', '.join(map(str, zapis))}")

# 6. Проверьте факт посещения по номеру карты
proverka_karty = 2140
if proverka_karty in poseshchenie:
    print(f"Пациент {proverka_karty} посетил врача")
else:
    print(f"Пациент {proverka_karty} не посетил врача")

poisk_karty = 2121
fio = baza_pacientov.get(poisk_karty, "Пациент не найден")
print(f"ФИО пациента {poisk_karty}: {fio}")
