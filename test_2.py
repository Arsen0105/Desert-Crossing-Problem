s = 1000
l = 1
v = 500

# Дальность поездки наодном бензобаке
max_car = v / l

# Количество бензобаков
n = 1
# Задача решается от конца, поэтому суммируем расстояние, которое проедем, расставив бензобаки в будущем 
stock = 0
while stock + max_car < s:
    stock += 1 / (1 + 2 * n) * max_car
    n += 1
    # print(n, stock, sep='\t\t')

print(n)
