#comentario
"""
  como vamos 
"""
'''

'''
nombre = 'sair'
cantidadMaterias = 3
numeroDecimal = 17.2

diasSemana = ['Lunes','Martes','Miercoles','Jueves','Viernes',] #lista = Array
listaDinamica = [0,'hola', 12.5, [0,1]]

diasSemana[2]

print(diasSemana[2]) # Miercoles
print(listaDinamica[3][1])  # [0,1] #1


esMayorEdad = False   #el booleano con mayuscula la primera letra

#Diccionarios - JSON - Objects
persona = {
   'nombre': 'Sair',
   'apellido': 'Botina',
   'edad':27,
   'materias': ['Base de datos II', 'lenguaje de cuarta generacion'],

}

print(persona['nombre']) #sair
print(persona['materias'][1]) #lenguaje de cuarta generacion

#lista de diccionarios 
personas =[ {
   'nombre': 'Sair',
   'apellido': 'Botina',
   'edad':27,
   'materias': ['Base de datos II', 'lenguaje de cuarta generacion'],

},
{
   'nombre': 'juan',
   'apellido': 'Botina',
   'edad':27,
   'materias': ['Base de datos II', 'lenguaje Orientado a Objeto'],

},
{
   'nombre': 'pepito',
   'apellido': 'Botina',
   'edad':27,
   'materias': ['Lenguaje Orientado a Eventos'],

}
]

print(personas[2]['materias'][0])  #lenguaje orientado a Eventos
#condiciones
esMayorEdad=True

if esMayorEdad==True:
   print('Es mayor de edad')
else:
   print('no es mayor de edad')


# for por in personas

for per in personas:
   print(per['nombre'])

nombrePersona ='roberto'
print(nombrePersona[2])


terminaciones = ['o','as','a','amos','ais','n']

verbo="caminar"

letraFinal = verbo[len(verbo)-1]
letraAntesFinal = verbo[len(verbo)-2]

terminacion = letraAntesFinal+letraFinal
verboSinTerminacion = verbo.replace(terminacion,"")

if terminacion=="ar":
   print("Yo "+verboSinTerminacion+"o")
   print("Tu "+verboSinTerminacion+"as")
   print("Él "+verboSinTerminacion+"a")
   print("Nosotros "+verboSinTerminacion+"amos")
   print("vosotros "+verboSinTerminacion+"ais")
   print("ellos "+verboSinTerminacion+"an")

elif terminacion=="er":
   print("Yo "+verboSinTerminacion+"o")
   print("Tu "+verboSinTerminacion+"es")
   print("Él "+verboSinTerminacion+"e")
   print("Nosotros "+verboSinTerminacion+"emos")
   print("vosotros "+verboSinTerminacion+"eis")
   print("ellos "+verboSinTerminacion+"en")

elif terminacion=="ir":
   print("Yo "+verboSinTerminacion+"o")
   print("Tu "+verboSinTerminacion+"es")
   print("Él "+verboSinTerminacion+"e")
   print("Nosotros "+verboSinTerminacion+"emos")
   print("vosotros "+verboSinTerminacion+"eis")
   print("ellos "+verboSinTerminacion+"en")
   