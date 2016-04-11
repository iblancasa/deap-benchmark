
import random
import time
import numpy
from deap import base
from deap import creator
from deap import tools
import sys


toolbox = None;

def evalOneMax(chromosome):
    return sum(chromosome),


def time_maxones(number, length):
    global toolbox
    inicioTiempo = time.clock()

    for i in range(number):
        best = creator.chromosome(random.getrandbits(1) for _ in range(length))
        toolbox.evaluate(best)

    return time.clock() - inicioTiempo


def main():
    global toolbox
    creator.create("fitness", base.Fitness, weights=(1.0,))

    if len(sys.argv)>1 and sys.argv[1]=="numpy":
        creator.create("chromosome", numpy.ndarray, fitness=creator.fitness)
    else:
        creator.create("chromosome", list, fitness=creator.fitness)
    toolbox = base.Toolbox()
    toolbox.register("evaluate", evalOneMax)


    length = 16
    iterations = 100000
    top_length = 32768

    while not length > top_length:
        print("deap-Onemax, " + str(length) +", "+ str(time_maxones( iterations, length)))
        length = length*2

if __name__ == "__main__":
    main()
