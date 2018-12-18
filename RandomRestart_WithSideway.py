import random
from copy import deepcopy
from collections import Counter
import CommonFunctions
#Common Functions required for all hill climbing are written here



def best_move_sideways(current_state,next_queen_positions_set, off_count, current_threat):
   # returns the configuration with heuristic less than or equal to the current heuristic
   #returns empty set if all the heuristics of neighbors are greater
   total = CommonFunctions.min_threat(current_state, next_queen_positions_set)
   min_of_threats = total[0]
   all_possible_moves = total[1]
   f_threats = total[2]


   if min_of_threats < current_threat :
       best_move_next = all_possible_moves[f_threats.index(min_of_threats)]
       off_count = off_count - 0
   elif min_of_threats == current_threat and off_count > 0:
       best_move_next = all_possible_moves[f_threats.index(min_of_threats)]
       off_count = off_count - 1
   else:
       best_move_next = []
       off_count = off_count - 0
   out = [best_move_next, off_count]
   return out

seq_count =[]

def hillclimbing(n, restart,sideway):
  '''Solving using hill climbing algorithm'''
  #Re generates a random configuration if there is failure to find a solution
  initial_state = CommonFunctions.initial_queen_positions(n)
  initial_threat = CommonFunctions.threats(initial_state)

  seq = []
  count = {}
  if (initial_threat) == 0:
      #exits hill climbing if goal is reached
      seq.append(initial_state)
      print("Initial state is Goal state ")
      print("Success")
      count["Success"] = len(seq)
      return count
  else:
      # assigns the initial state to a new state and gets heuristic
      current_state = initial_state
      current_threat = CommonFunctions.threats(current_state)
      while current_threat != 0:

          seq.append(current_state)
          current_state = deepcopy(current_state)
          next_queen_positions_set = CommonFunctions.next_possible_queen_positions(current_state)
          #expands neighbors until goal is reached
          current_state1 = best_move_sideways(current_state, next_queen_positions_set,sideway,current_threat)
          current_state = current_state1[0]
          sideway = current_state1[1]


          current_threat = CommonFunctions.threats(current_state)


          if current_state == []:
              # restarts if failure is returned
              a = restart+1
              restart = a
              seq_count.append(len(seq))
              hillclimbing(n,restart,sideway)


      count["Success"] = len(seq)
      out = [restart , count]
      return out

#Takes input from user
n = int(input("Enter the number of queens on the board : " ))
run_number_of_times = int(input("Number of times to be run: "))
sideway = int(input("No of side moves allowed: "))


restart_counter = []

while_counter = 0
sucess_steps = []
failure_steps = []

# Runs for the number of times specified by the user
while while_counter < run_number_of_times:
 # generates a random state with n queens and solves it using hillclimbing where sideway moves are allowed
  restart = restart_counter
  solution  = hillclimbing(n, 0,sideway)
  restarts = solution[0]
  restart_counter.append(restarts)
  solve = solution[1]

  if "Failure" in solve.keys():
      failure_steps.append(solve["Failure"])

  if "Success" in solve.keys():
      sucess_steps.append(solve["Success"])

  while_counter = while_counter+1


# prints results

print("sum of success steps :"+str(sum(sucess_steps)))
print("failure_steps")
print(failure_steps)
print("sum of failure steps: "+str(sum(failure_steps)))
l_success_steps = len(sucess_steps)
l_failure_steps = len(failure_steps)
if sucess_steps==[]:
  l_success_steps = 1
if failure_steps ==[]:
  l_failure_steps = 1
print()

print("Average restarts: " +str(sum(restart_counter)/len(restart_counter)) )

#prints average and percentages
print("Average number of steps for success: "+str((sum(sucess_steps)/l_success_steps)))
print("Average number of steps for failure: "+str((sum(failure_steps)/l_failure_steps)))
print("failure_percent: " +str((len(failure_steps)*100/run_number_of_times)))
print("success_percent: " +str((len(sucess_steps)*100/run_number_of_times)))