# -*- coding: utf-8 -*-
"""
Editor de Spyder
"""

import random
import time
import math

pistas1 = [[2,4,3,0,8,0,9,0,2,7,0,1,5,9,5,9,1],
[4,9,0,4,8,2,1,0,5,0,2,8,0,5,9,7,3],
[5,9,5,5,0,1,8,7,0,6,9,4,6,5,9,3,3],
[5,8,5,4,5,9,2,2,3,7,1,0,0,2,8,8,2],
[5,1,4,1,4,9,5,1,5,6,5,4,9,8,7,2,2],
[9,1,7,6,6,7,5,9,5,4,5,8,1,8,5,0,3],
[0,5,4,2,5,5,7,6,7,0,4,0,1,4,4,3,2],
[8,1,4,5,8,5,6,3,0,0,2,9,1,9,7,7,2],
[7,3,0,8,9,5,5,5,6,3,6,1,9,2,5,2,3],
[0,8,7,1,9,0,7,1,0,2,1,6,3,5,0,2,3],
[2,9,0,3,0,2,7,1,0,3,8,7,2,6,0,3,1],
[3,9,7,6,7,3,4,5,0,9,7,6,9,6,1,3,3],
[1,2,3,5,3,4,4,7,4,5,6,3,3,6,5,6,1],
[4,3,0,9,8,3,6,0,3,1,3,5,9,8,3,1,3],
[8,1,5,7,9,1,8,1,2,3,2,4,1,9,1,3,2],
[1,7,4,2,9,5,7,4,3,2,4,8,4,2,1,6,1],
[2,6,0,4,1,2,4,4,4,3,8,8,0,1,2,5,3],
[1,0,0,8,9,9,7,6,5,5,6,0,8,3,1,9,2],
[9,4,5,3,2,5,1,2,0,0,4,4,9,0,9,2,1],
[8,2,8,4,2,9,1,4,6,0,2,6,2,9,0,5,0],
[8,2,8,1,5,6,7,0,3,4,8,3,4,0,0,9,2],
[0,9,7,5,3,8,8,1,5,8,4,7,6,2,6,1,1]]

pistas2 = [[9,0,3,4,2,2],
           [7,0,7,9,4,0],
           [3,9,4,5,8,2],
           [3,4,1,0,9,1],
           [5,1,5,4,5,2],
           [1,2,5,3,1,1]]

pistas3 = [[5,6,1,6,1,8,5,6,5,0,5,1,8,2,9,3,2],
[3,8,4,7,4,3,9,6,4,7,2,9,3,0,4,7,1],
[5,8,5,5,4,6,2,9,4,0,8,1,0,5,8,7,3],
[9,7,4,2,8,5,5,5,0,7,0,6,8,3,5,3,3],
[4,2,9,6,8,4,9,6,4,3,6,0,7,5,4,3,3],
[3,1,7,4,2,4,8,4,3,9,4,6,5,8,5,8,1],
[4,5,1,3,5,5,9,0,9,4,1,4,6,1,1,7,2],
[7,8,9,0,9,7,1,5,4,8,9,0,8,0,6,7,3],
[8,1,5,7,3,5,6,3,4,4,1,1,8,4,8,3,1],
[2,6,1,5,2,5,0,7,4,4,3,8,6,8,9,9,2],
[8,6,9,0,0,9,5,8,5,1,5,2,6,2,5,4,3],
[6,3,7,5,7,1,1,9,1,5,0,7,7,0,5,0,1],
[6,9,1,3,8,5,9,1,7,3,1,2,1,3,6,0,1],
[6,4,4,2,8,8,9,0,5,5,0,4,2,7,6,8,2],
[2,3,2,1,3,8,6,1,0,4,3,0,3,8,4,5,0],
[2,3,2,6,5,0,9,4,7,1,2,7,1,4,4,8,2],
[5,2,5,1,5,8,3,3,7,9,6,4,4,3,2,2,2],
[1,7,4,8,2,7,0,4,7,6,7,5,8,2,7,6,3],
[4,8,9,5,7,2,2,6,5,2,1,9,0,3,0,6,1],
[3,0,4,1,6,3,1,1,1,7,2,2,4,6,3,5,3],
[1,8,4,1,2,3,6,4,5,4,3,2,4,5,8,9,3],
[2,6,5,9,8,6,2,6,3,7,3,1,6,8,6,7,2]]

pistas =pistas1



def individual(length):
    res = [None]*length
    for i in range(0,length):
        res[i] = random.randint(0,9)
    
    return res

def population(length, count):
    pop = [ individual(length) for x in range(count) ]
    return pop


def mutation(individual):
    
    
    rand1 = random.randint(0, len(individual)-1)
    rand2 = random.randint(0,9)
    
    res = individual
    res[rand1] = rand2
    
    return res



def twoPointCrossover(individual1, individual2):    
    rand1 = random.randint(0, len(individual1)-1)
    rand2 = random.randint(rand1, len(individual1)-1)
    res1=[]
    res1.extend(individual1[0:rand1])
    res1.extend(individual2[rand1:rand2])
    res1.extend(individual1[rand2:len(individual1)])

    
    return res1

def fitness(individual):
    res = 0.
    for i in range(0,len(pistas)):
        coinciden = coincidencias(individual,pistas[i])
        coincidenPista = (pistas[i])[len(pistas[i])-1]
        res+= abs( (coinciden) - (coincidenPista) )
        
    return res

def selection(population):
    population_len = len(population)
    corte = int(round(population_len/5))
    if(corte<=1):
      corte=2
    parte = [None]*corte
    fitnesses = [None]*population_len
    for i in range(population_len):
        fitnesses[i] = fitness(population[i])
    all = list(zip(fitnesses, population))
    all.sort(key=lambda tup: tup[0], reverse=False)
    sort_population = [x[1] for x in all]
    for x in range(corte):
        if(x < corte):
            parte[x] = sort_population[x]
        
    return parte
    
def coincidencias(individual, pista):    
    coincidencias = 0
    for i in range(0,len(individual)):
        if (individual[i] == pista[i]):
            coincidencias = coincidencias+1
    return coincidencias

def select_crossover(population):
    res = [None]*2
    random1 = random.randint(0,len(population)-1)
    random2 = random1
    while(random1==random2):
        random2 = random.randint(0,len(population)-1)
    
    res[0] = population[random1]
    res[1] = population[random2]
    
    return res

def mutate(population, chance):
    new_population = []
    for i in population:
        if chance > random.random():
            new_population.append(mutation(i))
        else:
            new_population.append(i)

    return new_population
    
    
def evolve(population, chance):
    population_len = len(population)
    parte = selection(population)
    new_len = population_len-len(parte)
    nueva_parte = [None]*new_len
    
    for i in range(new_len):
        individuals = select_crossover(parte)
        p1 = individuals[0]
        p2 = individuals[1]
        individual = twoPointCrossover(p1, p2)
        nueva_parte[i] = individual
        
    res = parte + nueva_parte
    res = mutate(res, chance)
    return res

def most_suited(population):
    population_len = len(population)
    fitnesses = [None]*population_len
    for i in range(population_len):
        fitnesses[i] = fitness(population[i])
        
    all = list(zip(fitnesses, population))
    all.sort(key=lambda tup: tup[0], reverse=False)
    sort_population = [x[1] for x in all]
    mostSuited = sort_population[0]

    return mostSuited

def grade_population(population):
    res = 0
    for i in range(len(population)):
        res += fitness(population [i])
    res = res/len(population)
    return res


def genetic_prob(ages, population_size, mut_chance, pruebas):
    time_start = time.time()
    
    if(population_size>1):
      c_len = len(pruebas[0])-1
      
      pop = population(c_len, population_size)
      
      grade = [None]*ages
      
      for i in range(ages):
          grade[i] = grade_population(pop)
          pop = evolve(pop, mut_chance)
          suited = most_suited(pop)
          if(fitness(suited)==0.0):
              timer = time.time() - time_start
              
              hours = math.floor(timer/3600)
              minutes = math.floor(timer/60) - hours*60
              seconds = timer - minutes*60 - hours*3600
      
      
              timeStr = str(hours) + 'h ' +  str(minutes)+ 'm ' + str(seconds) + 's '
              
              print('solucion encontrada en ' + timeStr + 'el resultado es:')
              print(suited)
              return {'grades' : grade, 'result' : suited, 'time' : timer}
          
      suited = most_suited(pop) 
      result = suited
      timer = time.time() - time_start
      
      hours = math.floor(timer/3600)
      minutes = math.floor(timer/60) - hours*60
      seconds = timer - minutes*60 - hours*3600
      
      
      timeStr = str(hours) + 'h ' +  str(minutes)+ 'm ' + str(seconds) + 's '
      
      print('Solucion no encontrada. Se ha tardado ' + timeStr + 'y el último resultado es:')
      print(str(suited) + ' con una puntuación de ' + str(fitness(suited)))
      return {'grades' : grade, 'result' : result, 'time' : time.time() - time_start}
     
    else:
        print('La población inicial debe ser de al menos 2 individuos, en otro caso no pueden realizarse cruces.')