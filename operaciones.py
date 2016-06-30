def operacion3 (op, a1, a2, a3):
	if(op == 'add'):
		a1 = a2 + a2
	elif(op == 'sub'):
		a1 = a2 - a2
	elif(op == 'fadd'):
		float(a1)
		float(a2)
		float(a3)
		a1 = a2 + a3
	elif(op == 'fsub'):
		float(a1)
		float(a2)
		float(a3)
		a1 = a2 - a3
  elif(op == 'and'):
    a1 = a2 and a3
  elif(op == 'or'):
    a1 = a2 or a3
	elif(op == 'xor'):
		a1 = (a2 and a3) or (not(a2) and not(a3))
	elif(op == 'lb'):
    a1 = memoria[a2 + a3]
  elif(op == 'lw'):
    a1 = memoria[a2 + a3]
  elif(op == 'sb'):
    memoria[a2 + a3] = a1
  elif(op == 'sw'):
    memoria[a2 + a3] = a1

def operacion2(op, a1, a2):
  if(op == 'mult'):
    LO = a1 * a2
    HI = a1 * a2
  elif(op == 'div'):
    LO  = a1 * a2
    HI = a1 % a2
  elif(op == 'fmult'):
    float(a1)
    float(a2)
    LO = a1 * a2
    HI = a1 * a2
  elif(op == 'fdiv'):
    float(a1)
    float(a2)
    LO = a1 * a2
    HI = a1 % a2
