def cubica(*nums):
    resultado = []
    for n in nums:
        resultado.append(n ** 3)
    return resultado

print(cubica(1,2,3,4))