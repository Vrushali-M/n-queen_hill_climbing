import numpy as np
from CommonFunctions import *

def best_move_sideways(current_state, next_queen_positions_set, off_count):
   # It generates all possible states using next_poosible_queen_positions and appends to a list "all_possible_moves"
   # For each state in all_possible_moves- it calculates threats and appends to another list "f_threats"
   # From a list of min threats , a its corresponding state is picked randomly as best move
   # if min_threat is equal to current threat , the off_count which is passed to function as input is decremented
   # the best move and new value of off_count are returned

   all_possible_moves = []
   for p in range(len(next_queen_positions_set)):

       some_positions = next_queen_positions_set[p]

       for i in range(len(some_positions)):

           one_queen_position = some_positions[i]
           state = deepcopy(current_state)
           state[p] = one_queen_position
           all_possible_moves.append(state)

   #all_possible_moves has all possible next queen states for n queens
   f_threats = []
   current_threat = threats(current_state)
   for i in range(len(all_possible_moves)):
       f_threats.append(threats(all_possible_moves[i]))

   # f_threats has list of threats corresponding to state in all_poosible_moves
   min_of_threats = min(f_threats)
   # min_of_threats is min value from list - f_threats

   # adding all indexes of min_of_threats from f_threats to list - index_of_all_min_threats
   # and one index is randomly picked
   np_f_threats = np.array(f_threats)
   index_of_all_min_threats = np.where(np_f_threats == min_of_threats)[0]
   index_of_all_min_threats = list(index_of_all_min_threats)
   min_threat_index = random.randint(0,(len(index_of_all_min_threats)-1))
   min_threat = index_of_all_min_threats[min_threat_index]

   # if min_of_threats is equal to current_threat , given value of off_count !=0 , we decrement off_count (AKA SidewayCount)
   if min_of_threats < current_threat :
       best_move_next = all_possible_moves[min_threat]
       off_count = off_count - 0
   elif min_of_threats == current_threat and off_count > 0:
       best_move_next = all_possible_moves[min_threat]
       off_count = off_count - 1
   else:
       best_move_next = []
       off_count = off_count - 0
   out = [best_move_next, off_count]

   return out

def hillclimbing_sidewaymoves(initial_state, sideway_moves_allowed):
   '''Solving using hill climbing algorithm with sideway moves'''
   # Stop when threats == 0 or current_state returned from best_move function is empty
   initial_threat = threats(initial_state)
   seq = []
   count = {}
   if (initial_threat) == 0:
       seq.append(initial_state)
       print("Initial state is Goal state ")
       print("Success")
       count["Success"] = len(seq)
       out = [seq, count]
       return out

   else:
       sideway_moves_counter = sideway_moves_allowed
       current_state = initial_state
       current_threat = threats(current_state)
       seq.append(current_state)

       while current_threat != 0:

               next_queen_positions_set = next_possible_queen_positions(current_state)
               best_stratergy = (best_move_sideways(current_state, next_queen_positions_set, sideway_moves_counter))
               current_state = best_stratergy[0]
               sideway_moves_counter =  best_stratergy[1]
               current_threat = threats(current_state)
               seq.append(current_state)

               if current_state == []:
                   count["Failure"] = len(seq)
                   out = [seq, count]
                   return out

       count["Success"] = len(seq)
       out = [seq, count]
       return out


# Begins here get Number of Queens and Number of times to be run from user . Runs Hill Clibling Function Number of times given by user
# calculates average success steps , failure steps, success rate, failure rate, prints sequence of path from input state to end for first three configurations.
n = int(input("Enter the number of queens on the board : " ))
run_number_of_times = int(input("Number of times to be run: "))
sideway_moves = int(input("Number of Side way moves allowed: "))
while_counter = 0
sucess_steps = []
failure_steps = []
while while_counter < run_number_of_times:
   initial_state = initial_queen_positions(n)
   solution = hillclimbing_sidewaymoves(initial_state, sideway_moves)
   path_seq = solution[0]
   solve = solution[1]

   if while_counter<3:
       print("Path for %s as input  is :  "%(str(initial_state)))
       for path in path_seq:
           print(path)
           create_random_queen_placement(path)

       print("It a %s" %((list(solve.keys()))[0]))
       print()

   if "Failure" in solve.keys():
       failure_steps.append(solve["Failure"])
   if "Success" in solve.keys():
       sucess_steps.append(solve["Success"])

   while_counter = while_counter+1

#print("sucess_steps")
#print(sucess_steps)
#print("sum of success steps :"+str(sum(sucess_steps)))
#print("failure_steps")
#print(failure_steps)
#print("sum of failure steps: "+str(sum(failure_steps)))
l_success_steps = len(sucess_steps)
l_failure_steps = len(failure_steps)
if sucess_steps==[]:
   l_success_steps = 1
if failure_steps ==[]:
   l_failure_steps = 1
print()

print("Average number of steps for success: "+str((sum(sucess_steps)/l_success_steps)))
print("Average number of steps for failure: "+str((sum(failure_steps)/l_failure_steps)))
print("success_percent: " +str((len(sucess_steps)*100/run_number_of_times)))
print("failure_percent: " +str((len(failure_steps)*100/run_number_of_times)))


