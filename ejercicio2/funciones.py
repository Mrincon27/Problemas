def producto_sencillo(x,y):
    if (len(x) == len(y)):
        producto = []
        a = 0
        for i in range(len(x)):
            b = 0
            b = x[i] * y[i]
            producto.append(b)
        for j in producto:
            a += j
        print(f"El producto de los arreglos entre numero1 y numeros 2es: {a}")
    else:
        print("La cantidad de items en los arreglos, no son iguales por favor coloque la misma cantidad")