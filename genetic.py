import random
from problems import Problem

class Genetic:
  POPULATION_SIZE = 250
  MAX_GEN = 100
  MUTATION_PROB = 0.1

  def __init__(self, problem: Problem) -> None:
    self.problem = problem
    self.n = problem.n
    self.max_fitness = (self.n * (self.n - 1)) // 2
    self.population = [problem.random_state() for _ in range(Genetic.POPULATION_SIZE)]
    self.gen = 0
    self.solution = None
  
  def fitness(self, chromosome):
    return self.max_fitness - self.problem.h(chromosome)

  def calc_prob(self, fitness):
    '''
      Calculate probabilty with current fitness
    '''
    return fitness / self.max_fitness

  def cross_over(self, chrom_1, chrom_2):
    n = len(chrom_1)
    split = random.randrange(0, n)
    child = chrom_1[:split] + chrom_2[split:]
    return child

  def mutate(self, chrom):
    pos = random.randrange(0, len(chrom))
    new_chrom = list(chrom)
    new_chrom[pos] = random.randrange(0, self.n)
    return tuple(new_chrom)
  
  def pretty_print(self):
    print(f"Population size: {Genetic.POPULATION_SIZE}")
    print(f"Mutation probability: {Genetic.MUTATION_PROB}")
    print(f"Solved in generation: {self.gen}")
    l = len(self.solution)
    for i in range(l):
      for j in range(l):
        if i == self.solution[j]:
          print("Q ", end='')
        else:
          print("* ", end='')
      print()

  def solve(self, no_limit=False):
    while no_limit or self.gen != Genetic.MAX_GEN:
      all_fitness = [self.fitness(chrom) for chrom in self.population]
      # print(all_fitness)
      if self.max_fitness in all_fitness:
        self.solution = self.population[all_fitness.index(self.max_fitness)]
        return

      # Calculate probabilitiy for each chromosome to be choosen for next generation
      self.probs = [self.calc_prob(f) for f in all_fitness]

      new_population = []
      
      for _ in range(len(self.population)):
        # Selection
        first, second = random.choices(self.population, weights=self.probs, k=2)
        
        # Cross-over
        child = self.cross_over(first, second)

        # Mutation
        if random.random() < Genetic.MUTATION_PROB:
          child = self.mutate(child)

        new_population.append(child)

      del self.population
      self.population = new_population
      self.gen += 1
