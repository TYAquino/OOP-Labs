def subtract(a,b):
    pass
cube = lambda num: num**3
print(type(cube))
print(cube(4))

power = lambda base, exp: base**exp
print(power(2,3))

l1 = [2,3,4,5]
cubes = map(cube,l1)
print(type(cubes))
print(cubes)
print(list(cubes))


