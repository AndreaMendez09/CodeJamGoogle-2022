t = int(input()) # Lee la primera linea
for i in range(1,t+1): # Primer bucle para los casos
    print("Case #{}: ".format(i), end="")
    c_list = []
    m_list = []
    y_list = []
    k_list = []
    for j in range (i*3,(i * 3) + 3): # Segundo bucle para los colores
      c,m,y,k = [int(s) for s in input().split(" ")]
      c_list.append(c)
      m_list.append(m)
      y_list.append(y)
      k_list.append(k)
    # Obtenemos los minimos y partimos desde ahi
    min_c = min(c_list)
    min_m = min(m_list)
    min_y = min(y_list)
    min_k = min(k_list) 
    if (min_c + min_m + min_y + min_k) < 1000000: # Si no hay color suficiente es imposible
        print("IMPOSSIBLE")
    elif (min_c + min_m + min_y + min_k) == 1000000: # Si da la casualidad de que suman exacto perfecto
        print("{} {} {} {}".format(min_c, min_m, min_y, min_k))
    else: # Sino calculamos una combinacion
        if (min_c >= 1000000):
            min_c = 1000000
            min_m = 0
            min_y = 0
            min_k = 0 
        elif (min_c + min_m >= 1000000):
            if min_m == 1000000 and min_c == 1000000:
                min_m = 0
            else:
                min_m -= (min_c + min_m) % 1000000;
            min_y = 0
            min_k = 0 
        elif (min_c + min_m + min_y >= 1000000):
            if min_y == 1000000 and (min_m == 1000000 or min_c == 1000000):
                min_y = 0
            else:
                min_y -= (min_c + min_m + min_y) % 1000000;
            min_k = 0 
        else:
            if min_k == 1000000  and (min_m == 1000000 or min_c == 1000000 or min_y == 1000000):
                min_k = 0
            else:
                min_k -= (min_c + min_m + min_y + min_k) % 1000000;
        print("{} {} {} {}".format(min_c, min_m, min_y, min_k)) #Imprimimos lo calculado