from consequenciaLogica import consequencia

def satisfazivel(formula):
	if consequencia([], ['~', formula]) == False:
		return True
	return False

formula1 = [['p'], '&', ['q']]
formula2 = [['p'], '&', ['~', ['p']]]

print(satisfazivel(formula1))
print(satisfazivel(formula2))