def calcular_cambio(monedas):

    tiposDeMonedas = [5, 2, 1]

    numeroDeMonedas = [0, 0, 0]

    i = 0
    
    for moneda in tiposDeMonedas:

            numeroDeMonedas[i] = cantidad // moneda # en python 3 necesitamos // para divisiones enteras
            cantidad = cantidad % moneda

            if cantidad  == 0:
                break
            else:
                i += 1

    return numeroDeMonedas



assert calcular_cambio(8) == (1,1,1)
#>>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
assert calcular_cambio(5) == (1,0,0)
#>>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
assert calcular_cambio(29) == (5,2,0)
#>>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.
assert calcular_cambio(29) == (0,0,0)
#>>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.