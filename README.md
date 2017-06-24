# Meta Heurística - Problema da mochila com CartolaFC

# Entendendo o problema
Para entendimento do problema, antes é necessario o conhecimento minimo sobre o jogo [CartolaFC](http://globoesporte.globo.com/cartola-fc/). 
No início de cada temporada, cada atleta ou treinador profissional do Campeonato Brasileiro recebe um valor virtual em cartoletas (moeda corrente para transações no jogo) e, de acordo com sua performance medida em pontos no decorrer das rodadas, tem seu preço valorizado ou desvalorizado. O usuário monta seu time inicial adquirindo onze atletas e um treinador, dentro do limite de seu orçamento (que, inicialmente, é de C$ 100, porém varia com o passar das rodadas e a valorização/desvalorização dos atleta escalados).
Supondo que N atletas tenham jogado nessa rodada e cada atleta tem atrelado a ele um preço, uma pontuação e uma posição:

| Atleta | Posição | Preço | Pontuação
| ------ | ------ | ------ | ------ |
| Jogador 1 | Atacante | 29.4 | 8.4 |
| Jogador 2 | Goleiro | 4.4 | 20.1 |
| ... | ... | ... | ... |
| Jogador 3 | Zagueiro | 5.1 | 3.9 |
| Jogador N | Meia | 2.1 | -3.4 |

Tendo N atletas e o valor disponivel em cartoletas montar o time com a maior pontuação possivel, respeitando a formação selecionada.
