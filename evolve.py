#!/usr/bin/env python

import random
import bisect

# These can be replaced to produce different genotypes, mutations, and trials

def initialise_genotypes():
    return (int(10 * random.random()) for i in xrange(10))

def mutate(i):
    return i + random.randint(-1, 1)

def trial(i):
    return -i

##################################################

def run_trials(population, trial_fn):
    return [(trial_fn(x), x) for x in population]

def create_next_population(population_with_fitness, mutate_fn):
    population_with_fitness.sort(key = lambda k : (k[0]))
    sorted_population = [x[1] for x in population_with_fitness]

    rank_selection = []
    j = 0
    max_relative_fitness = 0
    for i in xrange(len(sorted_population)):
        j += 1
        max_relative_fitness += j
        rank_selection.append(max_relative_fitness)

    new_population = []
    for i in xrange(len(sorted_population)):
        j = bisect.bisect(rank_selection, random.random() * max_relative_fitness)
        mutated_member = mutate_fn(sorted_population[j])
        new_population.append(mutated_member)

    return new_population

def start_evolving(initialise_genotypes_fn, mutate_fn, trial_fn):
    population = initialise_genotypes_fn()

    for i in xrange(1000): # 1000 generations
        population_with_fitness = run_trials(population, trial_fn)
        population = create_next_population(population_with_fitness, mutate_fn)

    for i in population:
        print i

def main():
    start_evolving(initialise_genotypes, mutate, trial)

if __name__ == "__main__":
    main()
