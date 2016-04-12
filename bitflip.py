
import random
import time
import numpy
from deap import base
from deap import creator
from deap import tools
import sys




def bitFlip(chromosome):
    mutation_point = random.randint(0,len(chromosome)-1)
    mutie = chromosome.copy()
    mutie[mutation_point] = not mutie[mutation_point]
    return mutie

def time_this(toolbox, number, chromosome):
    inicioTiempo = time.clock()

    for i in range(number):
        toolbox.mutate(chromosome)

    return time.clock() - inicioTiempo


def main():
    creator.create("fitness", base.Fitness, weights=(1.0,))

    if len(sys.argv) == 1:
        sys.argv.append("numpy")

    if sys.argv[1]=="numpy":
        creator.create("chromosome", numpy.ndarray, fitness=creator.fitness)
    else:
        creator.create("chromosome", list, fitness=creator.fitness)
        
    toolbox = base.Toolbox()

    if len(sys.argv)>2 and sys.argv[2]=="native":
        native = True
    else:
        native = False


    length = 16
    iterations = 100000
    top_length = 32768

    while not length > top_length:
        chromosome = creator.chromosome(random.getrandbits(1) for _ in range(length))
        indpb=1/length
        if native:
            toolbox.register("mutate", tools.mutFlipBit, indpb=indpb)
        else:
            toolbox.register("mutate", bitFlip)
        print("Python_DEAP_"+sys.argv[1]+"-BitVector, " + str(length) +", "+ str(time_this(toolbox, iterations, chromosome)))
        length = length*2

if __name__ == "__main__":
    main()
