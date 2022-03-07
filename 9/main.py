def naive_mul(x, y):
    if x < 0 and y < 0:
        x = abs(x)
        y = abs(y)
    r = 0
    for i in range(0, y):
        r = x + r
    return r
print(naive_mul(11, -15))

