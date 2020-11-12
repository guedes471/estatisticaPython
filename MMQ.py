class Ponto:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  #Função que gera a matriz do sistema, a partir das derivadas parciais
def coeficientes(pontos):
  n = len(pontos)
  somaXi = 0
  somaXi2 = 0
  somaYi = 0
  somaXiYi = 0
  for i in pontos:
    somaXi += i.x 
    somaXi2 += i.x ** 2
    somaYi += i.y 
    somaXiYi += i.x * i.y 
  
  return [[somaXi2, somaXi, somaXiYi],[somaXi, n, somaYi]]

#resolve o sistema e retorna os coeficientes da reta
def reta(M):
  somaX = (-1 * M[0][0] * M[1][1]) + (M[1][0] * M[0][1])
  resX = ((-1 * M[1][1] * M[0][2]) + (M[1][2] * M[0][1])) / somaX

  resY = (M[0][2] - (resX * M[0][0])) / M[0][1]

  return [resX, resY]

def residuos(pontos, a, b):
  res = []
  for p in pontos:
    res.append(p.y - a*p.x - b)
  
  return res

numero = int(input("Insira o numero de pontos"))
pontos = []
for i in range(numero):
  crd = input("Digite as coordenadas").split()
  p = Ponto(float(crd[0]), float(crd[1]))
  pontos.append(p)

M = coeficientes(pontos)
resultados = reta(M)
print("Reta:\n y = " + str(resultados[0]) + "x + " + str(resultados[1]) + "\n")

print("Os restos são:\n")
restos = residuos(pontos, resultados[0], resultados[1])

s = ""
for i in restos:
  s += " " + str(i)

print(s)




