class Individuo:
  def fitness(self):
    raise NotImplementedError("Implementar")

  def mutacao(self):
    raise NotImplementedError("Implementar")
  
  def crossover(self, b):
    raise NotImplementedError("Implementar")