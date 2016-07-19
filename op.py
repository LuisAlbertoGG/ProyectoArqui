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
ciclos = 0
operacion = array(["add", "sub", "mul", "div", "fadd", "fsub", "fmul", "fdiv", "and", "or", "xor", "not", "lb", "lw", "sb", "sw", "li", "b", "beqz", "bltz", "syscall"])
opHex = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", 10, 11, 12, 13, 14])


def op(array):
	if(array[0] == 'add'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		r[a] = r[b] + r[c]
		ciclos += 3
	elif(array[0] == 'sub'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		r[a] = r[b] - r[c]
		ciclos += 4
	elif(array[0] == 'mul'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		r[a] = r[b] * r[c]
		ciclos += 10
	elif(array[0] == 'div'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		r[a] = r[b] / r[c]
		ciclos += 11
	elif(r[0] == 'fadd'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		float(r[a])
		float(r[b])
		float(r[c])
		r[a] = r[b] + r[c]
		ciclos += 4
	elif(r[0] == 'fsub'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		float(r[a])
		float(r[b])
		float(r[c])
		r[a] = r[b] - r[c]
		ciclos += 5
	elif(array[0] == 'fmul'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		float(r[a])
		float(r[b])
		float(r[c])
		r[a] = r[b] * r[c]
		ciclos += 9
	elif(array[0] == 'fdiv'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		float(r[a])
		float(r[b])
		float(r[c])
		r[a] = r[b] / r[c]
		ciclos += 10
    elif(array[0] == 'and'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		r[a] = r[b] and r[c]
		ciclos += 1
    elif(array[0] == 'or'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		r[a] = r[b] or r[c]
		ciclos += 1
	elif(array[0] == 'xor'):
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		c = quitaCaract(array[3])
		r[a] = (r[b] and r[c]) or (not(r[b]) and not(r[3]))
		ciclos += 1
	elif(array[0] == 'not')
		a = quitaCaract(array[1])
		b = quitaCaract(array[2])
		r[a] = not(r[b])
		ciclos += 1
