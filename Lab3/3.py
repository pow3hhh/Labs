import time
for size in [10000, 100000, 1000000]:
    lst, st = list(range(size)), set(range(size))
    target, missing = size // 2, -1  # -1 точно нет в наборе
    
    t1 = time.perf_counter(); target in lst; t_l_yes = time.perf_counter() - t1
    t1 = time.perf_counter(); target in st;  t_s_yes = time.perf_counter() - t1
    t1 = time.perf_counter(); missing in lst; t_l_no = time.perf_counter() - t1
    t1 = time.perf_counter(); missing in st;  t_s_no = time.perf_counter() - t1
    
    # Размер, Список(есть), Множество(есть), Список(нет), Множество(нет)
    print(f"{size:8} | {t_l_yes:.8f} | {t_s_yes:.8f} | {t_l_no:.8f} | {t_s_no:.8f}")
