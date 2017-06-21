from random import uniform, choice
import json

def gera_data_aleatorio(n, file):
	atletas = []
	for i in range(0, n):
		atleta = {}
		atleta['preco'] = uniform(1.0, 25.0)
		atleta['pontuacao'] = uniform(-5.0, 5.0) + uniform(-5.0, 10.0) + uniform(1.0, 5.0)
		atleta['e'] = atleta['pontuacao']/atleta['preco']
		atleta['posicao'] = choice(['LAT', 'ZAG', 'MEC', 'ATA', 'GOL'])
		atletas.append(atleta)

	with open(file, 'w') as outfile:
			json.dump(atletas, outfile)

def get_data(file):
	with open(file) as outfile:
		return json.loads(outfile.read())
