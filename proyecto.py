#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from numpy import *
# len regresa tamaño de la lista  
# parametroo una lista 
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
print 'longitud de memoria: '+longitudDeMemoria 
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
	return temp
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
	
	lis = l.split("#") 
	#print lis[1]
	if lis[0].find("#")>0:
		l=[]
	else:
		
		return lis[0].strip()
print lecturaArchivo(nomArchivo)
 

 
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

#crea un archivo error.txt que contienen 
# un texto  que se pasa por parametros 
def volcado(error):

    archi=open('error.txt','w') # crear el archivo 
    archi=open('datos.txt','a') # lo abre 
    archi.write(error) # escribe en el archivo 
    archi.close() #cierra el archivo












