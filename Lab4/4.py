words = ["кот", "собака", "кот", "дом"]

# 1. Обычный цикл
len_dict = {}
for word in words:
    len_dict[word] = len(word)

# 2. Dict comprehension
len_dict_comp = {word: len(word) for word in words}

print(len_dict)
print(len_dict_comp)
