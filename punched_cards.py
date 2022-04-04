t = int(input()) # Lee la primera linea
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")] # Lee los enteros siguientes
  print("Case #{}:".format(i)) #Se imprime el caso
  #Multiplicamos las columnas
  r = (2*m) + 1
  c = (2*n) + 1
  for column in range(1, c + 1):
      for row in range (1, r + 1):
          if row <= 2 and column <= 2:
              print(".", end="")
          elif column % 2 == 0 and row % 2 == 0:
              #Aqui se imprime un punto
              print(".", end="")
          elif column % 2 != 0 and row % 2 == 0:
              #Aqui va el menos
              print("-", end="")
          elif column % 2 != 0 and row % 2 != 0:
              #Aqui va el mas
              print("+", end="")
          elif column % 2 == 0 and row % 2 != 0:
              #Aqui va el pipeline
              print("|", end="")
      print("") #Al acabar la iteración imprimimos la fila