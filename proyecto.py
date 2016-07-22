#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#!/usr/bin/env python -W ignore::VisibleDeprecationWarning
import warnings
import sys
from numpy import *


def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

# len regresa tamaño de la lista  
# parametroo una lista 
mem = array([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
r = array([0,0,0,0,0,0,0,0])		
a = array([0,0])
s = 0
ra = 0
pc = 0
sp = 0
operacion = array(["add", "sub", "mul", "div", "fadd", "fsub", "fmul", "fdiv", "and", "or", "xor", "not", "lb", "lw", "sb", "sw", "li", "b", "beqz", "bltz", "syscall"])
opHex = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", 10, 11, 12, 13, 14])
longitudDeMemoria =0
nomArchivo = '' 
print len( sys.argv )
print sys.argv
if len( sys.argv ) != 4:
	print 'faltan argumentos '
else:
	longitudDeMemoria = sys.argv[2]
	nomArchivo = sys.argv[3]
print 'longitud de memoria: ' + longitudDeMemoria 
print 'nom archivo: '+nomArchivo
#memoria = [None] * longitudDeMemoria
#print memoria[3]


#
#leer un archivo  quita todos lo comentario
# @ regresa un lista 
# donde cada nodo es una linea de codigo sin comentarios
#
def lecturaArchivo (nombreArchivo):
	#atributoas de el metodo
	lista =[ ]
	#abre el archivo 
	try:
		archivo = open(nombreArchivo)
		linea = archivo.readline()
	except Exception :
		print "error de archivo"
		sys.exit(1)
	linea = archivo.readline()

	while linea != '':
		
		
		#linea.strip() #quita tabuladores
		#verifica si es un comentario
		s= quitaComentario(linea)
		lista.append(s)
		#actualiza la lineallz
		linea = archivo.readline()

	
	temp = quitarBlancos(lista)
	archivo.close()
	t =divide(temp)
	return t

# divide la lista
#metodo auxiliar que divide cada renglon
def divide (lista):
	lis = []
	i =0
	for x in range(0, len(lista)):
		i = i+1
		e =lista[x].split()
		lis.append(e)
	return lis

# metodo auxiliar quita espacios en blaco
# de una lista 

def quitarBlancos(lista):
	lis= []
	for l in lista:
		#print 'l es : '+l
		if l != "":
			
			lis.append(l)
	
	return lis

#meto auxilair que quita los comentarios de
# una lista
def quitaComentario(l):
	
	l.strip() # quita tabulaciones y espacios en blanco
	
	lis = l.split(";") 
	#print lis[1]
	if lis[0].find(";")>0:
		l=[]
	else:
		
		return lis[0].strip()


def ejecutar(matriz):
	i = 0
	while(i < len(matriz)):
		op(matriz[i], matriz)
		i = i+1



def salirVM(num):

	if num == 0 :
		print "Ejecución completada exitosamente"
	elif num == 1:
		print "División entre cero"
	elif num == 2:
		print "Dirección de memoria invalida"
	elif num == 3:
		print "La memoria se agotó"
	elif num == 4:
		print "Número de registro inválido"
	elif num == 5:
		print "Operación inválida"
	elif num == 6:
		print "Llamada al sistema inválido"
	elif num == 7:
		print "Error al cargar el archivo"
	elif num == 8:
		print "Argumentos inválidos"
	else:
		print "error al salir"

#lee la posicion de  de el un arreglo 
# aplica la opcion que se
def syscall(num):
	 # lee de terminal y lo guarda en la la posicion de el arreglo
	 #un tipo entero
	if num == 0:
		a = int(raw_input())
		r[10]= a
	#leee de terminal y lo guarda en la posicion de el arreglo
	# un tipo de caracter el primero de la cadena 
	elif num == 1:
		b = raw_input()
		r[10] = b[0]
	#lee de terminal y lo guarda en la posicion de el arreglo 
	# un tipo flotante
	elif num == 2:
		c = float(raw_input())
		r[10] = c
	#lee de terminal y lo guarda en la posicion de el arreglo 
	# un tipo cadena
 	elif num == 3:
 		d = raw_input()
 		r[10] = d
 	 # muestra en la terminal 
	 #un tipo entero
	elif num == 4:
		print r[9]
	# muestra en la terminal 
	# un tipo de caracter el primero de la cadena
	elif num == 5:
		print r[9]
	#lee de terminal y lo guarda en la posicion de el arreglo 
	# un tipo flotante
	elif num == 6 :
		print r[9]
	#imprime la cadena 
	elif num == 7:
		print r[9]
		#sale de es sistema 
	elif num == 8:
		salirVM(0)
	else:
		print "error"

# crear la matriz nula 
# de 5 x n  
# 5 por el nmero de columnoas y 
# n el numero de lineas

def crearMatriz(n):
	filas  =n  
	columnas= 5 
	matriz = []
 	for i in range(filas):
 		a = ['']*columnas
		matriz.append(a)
	return matriz



# muestra una matriz 
def mostarMatriz(M):
	for i in range(len(M)):
 		print '[',
 		for j in range(len(M[i])):
 			print '{:>3s}'.format(str(M[i][j])),
 		print ']'

# llenar la matris con una lista 
# cada fila es una linea de codigo y las columnas
# son los espacios de una instruccion 

#def llenarMatris(lista):
	


#crea un archivo error.txt que contienen 
# un texto  que se pasa por parametros 
def volcado(error):

    archi=open('error.txt','w') # crear el archivo 
    archi=open('datos.txt','a') # lo abre 
    archi.write(error) # escribe en el archivo 
    archi.close() #cierra el archivo

    def quitaCaract(pal):
	w = ""
	for c in pal:
		if (c != "$" or c != "r"):
			w.append(c)
	return w

def quitaCaract(pal):
	#w = ""
	#for c in pal:
	#	if (c != "$" or c != "r"):
	#		w+=str(c)
	#return w
	pal = pal.translate(None, ',$')
	return pal


#Faltaron lb, lw, sb, sw
def op(array, matrizCompleta):
	global pc
	if(array[0] == '0'):
		a = int(array[1])
		b = int(array[2])
		c = int(array[3])
		mem[a] = mem[b] + mem[c]
		pc = pc + 3
	elif(array[0] == 'sub'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		c = int(quitaCaract(array[3]))
		r[a] = r[b] - r[c]
		pc = pc + 4
	elif(array[0] == 'mul'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		c = int(quitaCaract(array[3]))
		r[a] = r[b] * r[c]
		pc = pc + 10
	elif(array[0] == 'div'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		c = int(quitaCaract(array[3]))
		r[a] = r[b] / r[c]
		pc = pc + 11
	elif(r[0] == 'fadd'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		c = int(quitaCaract(array[3]))
		float(r[a])
		float(r[b])
		float(r[c])
		r[a] = r[b] + r[c]
		pc = pc + 4
	elif(r[0] == 'fsub'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		c = int(quitaCaract(array[3]))
		float(r[a])
		float(r[b])
		float(r[c])
		r[a] = r[b] - r[c]
		pc = pc + 5
	elif(array[0] == 'fmul'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		c = int(quitaCaract(array[3]))
		float(r[a])
		float(r[b])
		float(r[c])
		r[a] = r[b] * r[c]
		pc = pc + 9
	elif(array[0] == 'fdiv'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		c = int(quitaCaract(array[3]))
		float(r[a])
		float(r[b])
		float(r[c])
		r[a] = r[b] / r[c]
		pc = pc + 10
	elif(array[0] == 'and'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		c = int(quitaCaract(array[3]))
		r[a] = r[b] and r[c]
		pc = pc + 1
	elif(array[0] == 'or'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		c = int(quitaCaract(array[3]))
		r[a] = r[b] or r[c]
		pc = pc + 1
	elif(array[0] == 'xor'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		c = int(quitaCaract(array[3]))
		r[a] = (r[b] and r[c]) or (not(r[b]) and not(r[3]))
		pc = pc + 1
	elif(array[0] == 'not'):
		a = int(quitaCaract(array[1]))
		b = int(quitaCaract(array[2]))
		r[a] = not(r[b])
		pc = pc + 1
	elif(array[0] == '10'):
		a = int(array[1])
		mem[a] = int(array[2]) #<< 16
		#r[a] = r[a] or array[2] #<< 32
		pc = pc + 1500
	elif(array[0] == 'b'):
		a = busca(array, array[1])
		ejecuta(matrix, a)
		pc = pc + 1
	elif(array[0] == 'beqz'):
		a = int(quitaCaract(array[1]))
		b = int(busca(array, array[2]))
		if(a == 0):
			ejecuta(matrix, b)
		pc = pc + 4
	elif(array[0] == 'bltz'):
		a = int(quitaCaract(array[1]))
		b = busca(array, array[2])
		if(a < 0):
			ejecuta(matrix, b)
		pc = pc + 5
	elif(array[0] == 'syscall'):
		syscall()
		
#Quita los dos puntos		
def quitaPuntos(wo):
	w = ""
	for c in wo:
		if (c != ":"):
			w.append(c)
	return w
	
#Regresa el indice del renglón+1 donde esta la palabra buscada
def busca(array, palabra):
	for i in (0,3):
		for j in i:
			sin = quitaPuntos(j)
			if(sin == palabra):
				return j+1
				
#Ejecuta a partir de un renglon
def ejecuta(matriz, index):
	for list in (0,3):
		for l in list:
			if(list > index):
				op(list)


def prepararaux(renglon):
	if(renglon[0] == 'add'):
		renglon[0] = '0'
		renglon[1] = corres(renglon[1])
		renglon[2] = corres(renglon[2])
		renglon[3] = corres(renglon[3])
		return renglon
	elif(renglon[0] == 'sub'):
		renglon[0] = '1'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'mul'):
		renglon[0] = '2'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'div'):
		renglon[0] = '3'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'fadd'):
		renglon[0] = '4'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'fsub'):
		renglon[0] = '5'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'fmul'):
		renglon[0] = '6'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'fdiv'):
		renglon[0] = '7'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'and'):
		renglon[0] = '8'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'or'):
		renglon[0] = '9'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'xor'):
		renglon[0] = 'A'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'not'):
		renglon[0] = 'B'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'lb'):
		renglon[0] = 'C'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'lw'):
		renglon[0] = 'D'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'sb'):
		renglon[0] = 'E'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'sw'):
		renglon[0] = 'F'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'li'):
		renglon[0] = '10'
		renglon[1] = corres(renglon[1])
		return renglon
	elif(renglon[0] == 'b'):
		renglon[0] = '11'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'beqz'):
		renglon[0] = '12'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'bltz'):
		renglon[0] = '13'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	elif(renglon[0] == 'syscall'):
		renglon[0] = '14'
		renglon[1] = corres[1]
		renglon[2] = corres[2]
		renglon[3] = corres[3]
		return renglon
	else:
		salirVM(5)

def preparar(matriz):
	i = 0
	while(i < len(matriz)):
		matriz[i] = prepararaux(matriz[i])
		i = i+1
	return matriz

def corres(direccion):
	a = quitaCaract(direccion)
	if(a == 'r0'):
		return '0'
	elif(a == 'r1'):
		return '1'
	elif(a == 'r2'):
		return '2'
	elif(a == 'r3'):
		return '3'
	elif(a == 'r4'):
		return '4'
	elif(a == 'r5'):
		return '5'
	elif(a == 'r6'):
		return '6'
	elif(a == 'r7'):
		return '7'
	elif(a == 'a0'):
		return '8'
	elif(a == 'a1'):
		return '9'
	elif(a == 's0'):
		return '10'
	elif(a == 'ra'):
		return '11'
	else:
		salirVM(2)



resultado = lecturaArchivo(nomArchivo)
resultado1 = preparar(resultado)
ejecutar(resultado1)
print "El resultado es " , mem[1]
print "Tardo en ciclos ", pc












