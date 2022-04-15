abscissas = [float(x) for x in input().split()]
ordinates = [float(x) for x in input().split()]
applicates = [float(x) for x in input().split()]

print(all(map(lambda x, y, z: x**2 + y**2 + z**2 <= 4, abscissas, ordinates, applicates)))

# with zip
# print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))