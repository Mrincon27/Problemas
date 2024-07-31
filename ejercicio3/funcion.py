def producto_doble(x,y):
    if len(x) == len(y):
        producto2=[]
        for i in range(len(x)):
            a= x[i] * y[i]
            producto2.append(a)
        print(f"El producto de los arreglos entre numero1 y numeros 2es: {producto2}")
    else:
        print("La cantidad de items en los arreglos, no son iguales por favor coloque la misma cantidad")