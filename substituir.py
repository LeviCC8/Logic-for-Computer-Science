def substituir(A, A1, A2):
	if A1 == A:
		return A2
	if len(A) == 1:
		return A
	if A[0] == '~':
		return ['~', substituir(A[1], A1, A2)]
	if type(A[0]) == list:
		return [substituir(A[0], A1, A2), A[1], substituir(A[2], A1, A2)]
'''
A = [ [['p'], '&', ['~', [['p'], '>', ['~', ['q']]]]], '|', ['~', ['q']]]

print(A)
print(substituir(A, ['~', ['q']], ['z']))
'''