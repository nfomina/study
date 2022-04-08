m = float(input())
h = float(input())

imt = m/(h*h)

if imt < 18.5:
    print("Недостаточная масса")
elif imt <= 25:
    print("Оптимальная масса")
else:
    print("Избыточная масса")
