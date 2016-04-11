
import random
import time
import numpy
from deap import base
from deap import creator
from deap import tools
import sys


toolbox = None;


def time_maxones(number, chromosome):
    global toolbox
    inicioTiempo = time.clock()

    for i in range(number):
        toolbox.mutate(chromosome)

    return time.clock() - inicioTiempo


def main():
    global toolbox
    creator.create("fitness", base.Fitness, weights=(1.0,))

    if len(sys.argv)>1 and sys.argv[1]=="numpy":
        creator.create("chromosome", numpy.ndarray, fitness=creator.fitness)
    else:
        creator.create("chromosome", list, fitness=creator.fitness)
    toolbox = base.Toolbox()


    length = 16
    iterations = 100000
    top_length = 32768

    while not length > top_length:
        chromosome = creator.chromosome(random.getrandbits(1) for _ in range(length))
        indpb=1/length
        toolbox.register("mutate", tools.mutFlipBit, indpb=indpb)
        print("deap-Bitflip, " + str(length) +", "+ str(time_maxones( iterations, chromosome)))
        length = length*2

if __name__ == "__main__":
    main()
