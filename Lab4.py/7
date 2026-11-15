dates = ["01.05", "02.05", "03.05", "04.05"]
temperatures = [18, 23, 27, 21]
threshold = 22

# 1. Нумерованный журнал 
print("Нумерованный журнал:")
for i, (date, temp) in enumerate(zip(dates, temperatures), start=1):
    print(f"{i}. {date}: {temp}°C")

# 2. Список дней с температурой выше порога (list comprehension)
hot_days = [date for date, temp in zip(dates, temperatures) if temp > threshold]
print(f"\nДни с температурой выше {threshold}:")
print(hot_days)

# 3. Словарь дата -> температура (dict comprehension)
temp_dict = {date: temp for date, temp in zip(dates, temperatures)}
print("\nСловарь температур:")
print(temp_dict)
