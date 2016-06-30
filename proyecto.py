
#!/usr/bin/python
# -*- coding: latin-1 -*-
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
memoria = [None] * longitudDeMemoria
print memoria[3]


#
#leer un archivo  quita todos lo comentario
# @ regresa un lista 
# donde cada nodo es una linea de codigo sin comentarios
#
def lecturaArchivo (nombreArchivo):
	#atributoas de el metodo
	lista =[ ]
	#abre el archivo 
	archivo = open(nombreArchivo)
	linea = archivo.readline()

	while linea != '':
		
		
		#linea.strip() #quita tabuladores
		#verifica si es un comentario
		s= quitaComentario(linea)
		lista.append(s)
		#actualiza la lineallz
		linea = archivo.readline()

	
	temp = quitarBlancos(lista)
	return temp
# metodo auxiliar quita espacios en blaco
# de una lista 

def quitarBlancos(lista):
	lis= []
	for l in lista:
		#print 'l es : '+l
		if l != "":
			print l
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
	switcher = {
        0: print "Ejecución completada exitosamente",
        1: print "División entre cero",
        2: print "Dirección de memoria invalida",
        3: print "La memoria se agotó",
        4: print "Número de registro inválido",
        5: print "Operación inválida",
        6: print "Llamada al sistema inválido",
        7: print "Error al cargar el archivo",
        8: print "Argumentos inválidos",
    }
    return switcher.get(argument, print "Error al salir")
    volcar()

volcar




	










