import time

sizes = [10_000, 100_000, 1_000_000]

for size in sizes:
    #исходный список до начала замера
    data = list(range(size))
    
    #замер для цикла с append
    start = time.time()
    res = []
    for x in data:
        if x % 2 == 0:
            res.append(x**2)
    time_loop = time.time() - start
    
    #замер для list comprehension
    start = time.time()
    res_comp = [x**2 for x in data if x % 2 == 0]
    time_comp = time.time() - start
    
    print(f"Размер: {size}")
    print(f"  Цикл: {time_loop:.5f} сек")
    print(f"  Comprehension: {time_comp:.5f} сек")
