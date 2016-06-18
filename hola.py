#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
# len regresa tamaño de la lista  
# parametroo una lista 
memoria =0
nomArchivo = '' 
print len( sys.argv )
print sys.argv
if len( sys.argv ) != 4:
	print 'faltan argumentos '
else:
	memoria = sys.argv[2]
	nomArchivo = sys.argv[3]
print 'memoria: '+memoria 
print 'nom archivo: '+nomArchivo


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




	

