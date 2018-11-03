import random

class Terms:
	forma1 = {
		'fem': ['República','Democracia','Monarquía'],
		'masc':  ['Estado','Gobierno']
	}      
	forma2 = {
		'fem': [
			'parlamentaria', 
			'socialista',
			'provisional', 
			'absoluta', 
			'constitucional', 
			'islámica parlamentaria', 
			'islámica presidencialista',
			'presidencialista',
			'semipresidencialista',
			'unipartidista'
		],
		'masc':	[
			'unipartidista',
			'semipresidencialista',
			'constitucional', 
			'islámico parlamentario', 
			'islámico presidencialista',
			'parlamentario', 
			'socialista'
		]
	}
  
list_fem1 = Terms.forma1['fem']
list_fem2 = Terms.forma2['fem']

list_masc1 = Terms.forma1['masc']
list_masc2 = Terms.forma2['masc']

fem_terms = (random.choice(list_fem1) + ' ' + random.choice(list_fem2)) 
masc_terms = (random.choice(list_masc1) + ' ' + random.choice(list_masc2))

final_terms = [fem_terms, masc_terms]
print(random.choice(final_terms))