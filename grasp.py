from data import *
import random

data_teste = get_data('teste.json')
MAX_V = 60
DOMINANTES = []

def teste_solucao(solucao, novo_elemento):
	if len(solucao) == 11:
		return False

	valor = sum(x['preco'] for x in solucao) + novo_elemento['preco']
	if valor > MAX_V:
		return False
	
	return True

def nova_solucao(solucao, a, preferenias, dominantes):
	# buscando elementos nao contidos na solucao, ordedando por 'e'
	candidatos = [x for x in data_teste if x not in solucao]
	candidatos.sort(key=lambda x: x['e'], reverse=True)
	# limitando a porcentagem de a
	quantidade_candidatos = int(a * len(candidatos))
	candidatos = candidatos[0:quantidade_candidatos]
	# selecionando aleatoriamente um elemento entre os canditatos
	elemento_atual = random.choice(candidatos)
	# enquanto nao sair do objetivo eu contiue adicionando aleatoriamente
	while teste_solucao(solucao, elemento_atual) == True:
		solucao.append(elemento_atual)
		candidatos = [x for x in candidatos if x is not elemento_atual]
		elemento_atual = random.choice(candidatos)

	for elemento_atual in candidatos:
		if len(solucao) == 11:
			break

		if teste_solucao(solucao, elemento_atual) == True:
			solucao.append(elemento_atual)
			candidatos = [x for x in candidatos if x is not elemento_atual]

	if len(solucao) == 11:
		dominantes.append(solucao)

	return solucao

#def busca_local(solucao, a, preferenias, dominantes):


nova_solucao([], 0.6, 0, DOMINANTES)
print(DOMINANTES)