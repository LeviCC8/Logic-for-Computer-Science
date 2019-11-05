from satisfazivel import satisfazivel

def restricao(restricoes):
	if len(restricoes) == 1:
		return restricoes[0]
	return [restricoes[0], '&', restricao(restricoes[1:])]


restricoes = [
				['p1'],
				['~', ['p2']],
				['~', ['p3']],
				['~', ['p4']],
				[[['p1'], '&', ['~', ['p4']]], '|', [['~', ['p1']], '&', ['p4']]],
				[[['p2'], '&', ['~', ['p3']]], '|', [['~', ['p2']], '&', ['p3']]],
			 ]


print(restricao(restricoes))

print(satisfazivel(restricao(restricoes)))