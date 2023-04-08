def armar_lista(nomb):
  nomb = nomb.replace("'", "")
  nomb = nomb.replace(",", " ")
  return nomb.split() #genero una lista a partir del string de nombres, quitando las comas y las comillas simples, y separando las palabras mediante el .split que separa por espacios

def punto1_generar (nomb, n1, n2):
  return dict(zip(nomb, list(zip(n1, n2))))

def punto2_promedio(diccionario):
  promedios = {}
  for estu in diccionario:
    promedios[estu] = sum(diccionario[estu]) / len(diccionario[estu])
  return promedios

def punto3_promedio_general(dicc_promedios):
  return sum(dicc_promedios.values()) / len(dicc_promedios) if (len(dicc_promedios) > 0) else 0

def punto4_promedio_mas_alto(dicc_promedios):
  return max(dicc_promedios.items(), key= lambda estu: estu[1])[0] # para que devuelva solo el nombre

def punto5_nota_mas_baja(diccionario):
  return min(diccionario, key= lambda estu: min(diccionario[estu])) # para que devuelva solo el nombre


nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''


notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 
           13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 
           74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8,
           87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31,
           39, 15, 74, 33, 57, 10]


lista = armar_lista(nombres) # primero armo una lista en limpio con los nombres de los estudiantes

estudiantes = punto1_generar(lista, notas_1, notas_2) # PUNTO 1 -> llamo a la funcion que genera un diccionario, con los nombres como claves, y ambas notas como valores

promedios = punto2_promedio(estudiantes) # PUNTO 2 -> llamo a la funcion que utiliza el diccionario anteriormente creado, genera uno nuevo con el promedio de ambas notas

print(f"El promedio general del curso es de: {round(punto3_promedio_general(promedios), 3)}") # PUNTO 3 -> llamo a la funcion que me devuelve un promedio de todos los promedios

nombre_max_promedio = punto4_promedio_mas_alto(promedios) # PUNTO 4 -> llamo a la funcion que retorna el nombre y la nota de aquella persona con el mayor promedio
print(f"El estudiante con la nota promedio mas alta, de {promedios.get(nombre_max_promedio)}, es {nombre_max_promedio}")

nombre_min = punto5_nota_mas_baja(estudiantes) # PUNTO 5 -> llamo a la funcion que retorna el nombre y la nota de aquella persona con la nota más baja
print(f"El estudiante con la nota mas baja, de {min(estudiantes.get(nombre_min))}, es {nombre_min}")