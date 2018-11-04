import random

class TermsGenerator:

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

	def _randomize(self):
		term_gender = random.choice(list(self.forma1.keys()))
		first_term = random.choice(self.forma1[term_gender])
		second_term = random.choice(self.forma2[term_gender])
		return ' '.join([first_term, second_term])

