s = 1000
l = 1
v = 500

max_car = v / l

n = 1
bank = 0
while bank + max_car < s:
    bank += 1 / (1 + 2 * n) * max_car
    n += 1
    # print(n, bank, sep='\t\t')

print(n)
