def valorVerdade(A, interpretacao):
	if len(A) == 1:
		for i in interpretacao:
			if i[0] == A[0]:
				return i[1]
	if A[0] == '~': 
		return not valorVerdade(A[1], interpretacao)
	if A[1] == '&': 
		return valorVerdade(A[0], interpretacao) and valorVerdade(A[2], interpretacao)
	if A[1] == '|': 
		return valorVerdade(A[0], interpretacao) or valorVerdade(A[2], interpretacao)
	if A[1] == '>': 
		return False if valorVerdade(A[0], interpretacao) == True and valorVerdade(A[2], interpretacao) == False else True
	if A[1] == '~&': 
		return False if valorVerdade(A[0], interpretacao) == True and valorVerdade(A[2], interpretacao) == True else True
	if A[1] == '~|':
		return True if valorVerdade(A[0], interpretacao) == False and valorVerdade(A[2], interpretacao) == False else False
	if A[1] == '<->': 
		return valorVerdade(A[0], interpretacao) == valorVerdade(A[2], interpretacao)
	if A[1] == '^': 
		return valorVerdade(A[0], interpretacao) ^ valorVerdade(A[2], interpretacao)
'''
A = [[['t'], '&', ['~', ['x']]], '>', ['a']]
B = [ [['~', ['p']], '&', ['~', [['p'], '>', ['~', ['q']]]]], '^', ['~', ['q']]]
interpretacao = {
	('t', True),
	('x', False),
	('a', False),
	('p', False),
	('q', False)
}

print(valorVerdade(A, interpretacao))
print(valorVerdade(B, interpretacao))
'''