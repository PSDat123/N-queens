from problems import Problem

class Genetic:
  POPULATION_SIZE = 10
  MAX_GEN = 2
  MUTATION_PROB = 0.1

  def __init__(self, problem: Problem) -> None:
    self.problem = problem
    self.max_fitness = problem.max_h()
    self.population = [problem.random_state() for _ in range(Genetic.POPULATION_SIZE)]
    self.gen = 1
  
  def fitness(self, chromosome):
    return self.max_fitness - self.problem.h(chromosome)

  def calc_prob(self, fitness):
    '''
      Calculate probabilty with current fitness
    '''
    return fitness / self.max_fitness

  def solve(self):
    while self.gen != Genetic.MAX_GEN:
      all_fitness = [self.fitness(chrom) for chrom in self.population]
      if self.max_fitness in all_fitness:
        return self.population[self.population.index(self.max_fitness)]

      # Calculate probabilitiy for each chromosome to be choosen for next generation
      self.probs = [self.calc_prob(f) for f in all_fitness]

      
      print(self.probs)
      
      # Choose the best chromosome
      # best_fitness = 0
      # best_index = 0
      # for i, fitness in enumerate(all_fitness):
      #   if fitness > best_fitness:
      #     best_fitness = fitness
      #     best_index = i
      
      # best_chromosome = self.population[best_index]
      



      self.gen += 1
