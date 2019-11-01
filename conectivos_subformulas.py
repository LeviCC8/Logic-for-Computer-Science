def conectivos(A):
	if A[0] == '~':
		return 1 + conectivos(A[1])
	if len(A) == 1:
		return 0
	if type(A[0]) == list:
		return 1 + conectivos(A[0]) + conectivos(A[2])

def subformulas(A):
	if A[0] == '~':
		return [A] + subformulas(A[1])
	if len(A) == 1:
		return [A]
	if type(A[0]) == list:
		return [A] + subformulas(A[0]) + subformulas(A[2])
'''
A = [[['t'], '&', ['~', ['x']]], '>', ['a']]

print(conectivos(A))
subf = subformulas(A)
for i in subf:
	print(i)
'''