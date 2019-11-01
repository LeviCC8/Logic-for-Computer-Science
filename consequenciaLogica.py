from atom_qtdAtom import atom
from valorVerdade import valorVerdade

def tabela_conquesencia(premissas, formula, atomicas, interpretacao):
	if atomicas == set():
		if valorVerdade(formula, interpretacao):
			return True
		valorPremissas = True
		for premissa in premissas:
			valorPremissas = valorPremissas and valorVerdade(premissa, interpretacao)
		return not valorPremissas
	atomica = atomicas.pop()
	interpretacao1 = interpretacao.union({(atomica, True)})
	interpretacao2 = interpretacao.union({(atomica, False)}) 
	return tabela_conquesencia(premissas, formula, atomicas.copy(), interpretacao1) and tabela_conquesencia(premissas, formula, atomicas.copy(), interpretacao2)

def consequencia(premissas, formula):
	atomicas = atom(formula)
	for premissa in premissas:
		atomicas = atomicas.union(atom(premissa))
	interpretacao = set()
	return tabela_conquesencia(premissas, formula, atomicas, interpretacao)
'''
premissas = [
			['p'], 
			['q']
			]
formula = [[['p'], '>', ['q']], '&', ['r']]
print(consequencia(premissas, formula))
'''