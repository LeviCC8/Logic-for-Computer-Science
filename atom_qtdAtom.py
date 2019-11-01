def qtdAtom(A):
	if A[0] == '~':
		return qtdAtom(A[1])
	if len(A) == 1:
		return 1
	if type(A[0]) == list:
		return qtdAtom(A[0]) + qtdAtom(A[2])

def atom(A):
	if A[0] == '~':
		return atom(A[1])
	if len(A) == 1:
		return set(A)
	if type(A[0]) == list:
		return atom(A[0]).union(atom(A[2]))
'''
A = [ [['p'], '&', ['~', [['p'], '>', ['~', ['q']]]]], '|', ['~', ['q']]]

print(qtdAtom(A))
print(atom(A))
'''