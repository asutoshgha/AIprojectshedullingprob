class Data:

class Population:
    def __init__(self,size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0,size): self._schedules.append(Schedule().initialise())
    def get_schedules(self): return self._schedules

class GeneticAlgo:

    def evolve(self, population): return self._mutate_population(self._crossover_population(population))
    def crossover_population(self,pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = OF ELITE SCHEDULES
        while i < POPULATION SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0])
            schedule2 = self._select_tournament_population(pop).get_schedules()[0])
            crossover_pop.get_schedules().append(self._crossover_schedulele(schedule1,schedule2))
            i+=1
            
       return crossover _ pop
    def _mutate_population(self,population) :
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population
    def _crossover_scheule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(O,len(crossoverSchedule.get_classes())):
            if (rnd.random()>0.5: crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else: crossoverSchedule.get_classes()[i] =schedule2.get_classes()[i]
         return crossoverScheduIe

    def _mutate_schedule(self, mutateSchedule):
    
         schedule = Schedule().initialize()
         for i in range(0,len(mutateSchedule.get_classes())):
              if(MUTATION_RATE > rnd.random(): mutateSchedule.get_classes()[i] + schedule.get_classes()[i]
         return mutateSchedule
    def _select_tournament_population(self,pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
           tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE])
            i+=1
         tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
         return tournament_pop
        
         

class Course:
    def __init__(self,number,name,instructors,maxNumOfStudents):
        self._number=number
        self._name=name
        self._maxNumOfStudents=maxNumOfStudents
        self._instructors=instructors


class Instructor:

class Room:

class Meetingtime:

class Department:

class Class:


