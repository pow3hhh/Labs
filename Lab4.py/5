students = [
    {"name": "Анна", "score": 85, "attempts": 2},
    {"name": "Иван", "score": 55, "attempts": 1},
    {"name": "Олег", "score": 90, "attempts": 4},
    {"name": "Мария", "score": 70, "attempts": 3}
]

# 1. Обычный цикл с append()
ord_c = []
for st in students:
    if st["score"] >= 60 and st["attempts"] <= 3:
        ord_c.append(st["name"])

# 2. List comprehension
c_comp = [st["name"] for st in students if st["score"] >= 60 and st["attempts"] <= 3]

print(ord_c)
print(c_comp)
