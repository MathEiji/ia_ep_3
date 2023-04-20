from pop_ladra import PopLadra
from cidades import Cidades
from geneticos.algoritmo_genetico_populacao import AlgoritmoGeneticoPopulacao


populacao = PopLadra(Cidades, 10)
genetico = AlgoritmoGeneticoPopulacao(populacao)
individuo_adaptado = genetico.rodar(False)
print("\nPrimeiro mais adaptado sem crossover:")
print(f"Quantidade de gerações: {genetico.qtd_geracoes()}")
print(individuo_adaptado.imprime())

populacao = PopLadra(Cidades, 10)
genetico = AlgoritmoGeneticoPopulacao(populacao)
individuo_adaptado = genetico.rodar(True)
print("\nPrimeiro mais adaptado com crossover:")
print(f"Quantidade de gerações: {genetico.qtd_geracoes()}")
print(individuo_adaptado.imprime())

