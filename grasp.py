from data import *
from copy import copy, deepcopy
import random

data_teste = get_data('teste.json')
MAX_V = 100
DOMINANTES = []


def printa_solucao(arr):
	for elemento in arr:
		print(elemento)

def f(arr, tipo):
	r = 0
	for elemento in arr:
		r+= elemento[tipo]
	return r

def ajusta_array(arr):
	candidatos_max_element = [x for x in data_teste if x not in arr]
	max_element = max(candidatos_max_element, key=lambda d: d['preco'])
	preco_atual = f(arr, 'preco')
	for elemento in arr:
		if elemento['marcado'] == False:
			preco_atual -= elemento['preco']
			arr.remove(elemento)
			if MAX_V - preco_atual >= max_element:
				break
	return arr

def hasElemento(arr):
	for elemento in arr:
		if elemento['marcado'] == False:
			return True
	return False

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

def busca_local(solucao, a, preferenias, dominantes):
	solucao_aux = deepcopy(solucao)
	solucao_aux.sort(key=lambda x: x['e'], reverse=True)

	for elemento in solucao_aux:
		elemento['marcado'] = False

	while hasElemento(solucao_aux):
		print(f(solucao, 'pontuacao'))
		solucao_ajustada = ajusta_array(deepcopy(solucao_aux))
		solucao_nova = nova_solucao(deepcopy(solucao_ajustada), a, preferenias, dominantes)

		if f(solucao_nova, 'pontuacao') > f(solucao, 'pontuacao'):
			solucao = deepcopy(solucao_nova)
			for elemento in solucao_aux:
				elemento['marcado'] = False
		else:
			for elemento in solucao_aux:
				if elemento['marcado'] == False:
					elemento['marcado'] = True
					break


arr = nova_solucao([], 0.6, 0, DOMINANTES)
busca_local(arr, 0.6, 0, DOMINANTES)
