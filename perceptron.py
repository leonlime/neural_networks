entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(entradas, pesos):
  s = 0
  for i in range(3):
    print(entradas[i])
    print(pesos[i])
    s += entradas[i] * pesos[i]
  return s

s = soma(entradas, pesos)
print(s)

def stepFunction(soma):
  if (soma >= 1):
    return 1
  return 0

r = stepFunction(s)
print(r)