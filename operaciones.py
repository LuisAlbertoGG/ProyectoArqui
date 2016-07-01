def op(array):
	if(array[0] == 'add'):
		array[1] = array[2] + array[3]
		ciclos += 3
	elif(op == 'sub'):
		array[1] = array[2] - array[3]
		ciclos += 4
	elif(op == 'mul'):
		array[1] = array[2] * array[3]
		ciclos += 10
	elif(op == 'div'):
		array[1] = array[2] / array[3]
		ciclos += 11
		
	elif(op == 'fadd'):
		float(array[1])
		float(array[2])
		float(array[3])
		array[1] = array[2] + array[3]
		ciclos += 4
	elif(op == 'fsub'):
		float(array[1])
		float(array[2])
		float(array[3])
		array[1] = array[2] - array[3]
		ciclos += 5
	elif(op == 'fmul'):
		float(array[1])
		float(array[2])
		float(array[3])
		array[1] = array[2] * array[3]
		ciclos += 9
	elif(op == 'fdiv'):
		float(array[1])
		float(array[2])
		float(array[3])
		array[1] = array[2] / array[3]
		ciclos += 10
	
    elif(op == 'and'):
        array[1] = array[2] and array[3]
		ciclos += 1
    elif(op == 'or'):
        array[1] = array[2] or array[3]
		ciclos += 1
	elif(op == 'xor'):
		array[1] = (array[2] and array[3]) or (not(array[2]) and not(array)[3]))
		ciclos += 1
	elif(op == 'not')
		#a = m[pc + 3];
		array[1] = not(a2)
		ciclos += 1
