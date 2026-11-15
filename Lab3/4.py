import sys
#Создание словаря
user_dict = {
    101: "Иван Иванов, инженер",
    102: "Пётр Петров, дизайнер",
    103: "Анна Сидорова, аналитик"
}
# Получение значения по известному ключу
known_key = 102
print(f"Поиск по ключу {known_key}: {user_dict.get(known_key)}")

#Сравнение веса пустого списка, кортежа, множества и словаря
empty_list = []
empty_tuple = ()
empty_set = set()
empty_dict = {}




print("Размер пустых контейнеров в памяти (байты):")
print(f"Список (`list`): {sys.getsizeof(empty_list)} байт")
print(f"Кортеж (`tuple`): {sys.getsizeof(empty_tuple)} байт")
print(f"Множество (`set`): {sys.getsizeof(empty_set)} байт")
print(f"Словарь (`dict`): {sys.getsizeof(empty_dict)} байт")
