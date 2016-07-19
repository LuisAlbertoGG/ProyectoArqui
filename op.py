#!/usr/bin/python
from numpy import *

print("Hola")

longitudDeMemoria = 5
r = array([0,0,0,0,0,0,0,0])		
a = array([0,0])
s = 0
ra = 0
pc = 0
sp = 0
operacion = array(["add", "sub", "mul", "div", "fadd", "fsub", "fmul", "fdiv", "and", "or", "xor", "not", "lb", "lw", "sb", "sw", "li", "b", "beqz", "bltz", "syscall"])
opHex = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", 10, 11, 12, 13, 14])


memoria = array([0,0,0,0])

def op(array):
	if(array[0] == 'add'):
		array[1] = array[2] + array[3]
		ciclos += 3
	elif(array[0] == 'sub'):
		array[1] = array[2] - array[3]
		ciclos += 4
	elif(array[0] == 'mul'):
		array[1] = array[2] * array[3]
		ciclos += 10
	elif(array[0] == 'div'):
		array[1] = array[2] / array[3]
		ciclos += 11
	elif(array[0] == 'fadd'):
		float(array[1])
		float(array[2])
		float(array[3])
		array[1] = array[2] + array[3]
		ciclos += 4
	elif(array[0] == 'fsub'):
		float(array[1])
		float(array[2])
		float(array[3])
		array[1] = array[2] - array[3]
		ciclos += 5
	elif(array[0] == 'fmul'):
		float(array[1])
		float(array[2])
		float(array[3])
		array[1] = array[2] * array[3]
		ciclos += 9
	elif(array[0] == 'fdiv'):
		float(array[1])
		float(array[2])
		float(array[3])
		array[1] = array[2] / array[3]
		ciclos += 10
    elif(array[0] == 'and'):
        array[1] = array[2] and array[3]
		ciclos += 1
    elif(array[0] == 'or'):
        array[1] = array[2] or array[3]
		ciclos += 1
	elif(array[0] == 'xor'):
		array[1] = (array[2] and array[3]) or (not(array[2]) and not(array)[3]))
		ciclos += 1
	elif(array[0] == 'not')
		array[1] = not(array[2])
		ciclos += 1
	elif(array[0] == 'lb'):
		array[1] = memoria[array[2] + array[3]]
		ciclos += 500
	elif(array[0] == 'lw'):
		array[1] = memoria[array[2] + array[3]]
		ciclos += 1500
	elif(array[0] == 'sb'):
		memoria[array[2] + array[3]] = array[1]
		ciclos += 700
	elif(array[0] == 'sw'):
		memoria[array[2] + array[3]] = array[1]
		ciclos += 2100
	elif(array[0] == 'li'):
		array[1] = array[2] << 16
		array[1] = array[1] | array[2]
		ciclos += 2100
	#beq
	elif(array[0] == 'b'):
		beq(0, 0, array[1])
		ciclos += 1
	#beq
	elif(array[0] == 'beqz'):
		beq(array[1], 0, array[2])
		ciclos += 4
	#Falta cargar a la dirección en la posición array[2]
	elif(array[0] == 'bltz'):
		if(array[1] <= 0):
			array[2]
		ciclos += 5
	#Implementación
	elif(array[0] == 'syscall'):
		ciclos += 50
		
#Falta cargar a la dirección en la posición pos2
def beq(pos, num, pos2):
	if(pos == num):
		pos2
