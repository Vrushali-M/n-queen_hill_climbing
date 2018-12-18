from CommonFunctions import *


def best_move(current_state,next_queen_positions_set):
   #It generates all possible states using next_poosible_queen_positions and appends to a list
   #For each state in list it calculates threats and appends to another list
   #A state with min threat is picked as best move and returned
   all_possible_moves = []
   for p in range(len(next_queen_positions_set)):

       some_positions = next_queen_positions_set[p]

       for i in range(len(some_positions)):

           one_queen_position = some_positions[i]
           state = deepcopy(current_state)
           state[p] = one_queen_position
           all_possible_moves.append(state)

   #all_possible_moves has all possible next quuen states for n quuens
   f_threats = []
   current_threat = threats(current_state)
   for i in range(len(all_possible_moves)):
       f_threats.append(threats(all_possible_moves[i]))

   min_of_threats = min(f_threats)

   if min_of_threats < current_threat:
       best_move_next = all_possible_moves[f_threats.index(min_of_threats)]

   else:
       best_move_next = []

   return  best_move_next

def hillclimbing(initial_state):
   '''Solving using hill climbing algorithm'''
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
       current_state = initial_state
       current_threat = threats(current_state)
       seq.append(current_state)

       while current_threat != 0:
           next_queen_positions_set = next_possible_queen_positions(current_state)
           current_state = best_move(current_state, next_queen_positions_set)
           current_threat = threats(current_state)
           seq.append(current_state)

           if current_state == []:
               count["Failure"] = len(seq)
               out = [seq,count]
               return out


       count["Success"] = len(seq)
       out = [seq, count]
       return out


# Begins here get Number of Queens and Number of times to be run from user . Runs Hill Climbling Function Number of times given by user
# calculates average success steps , failure steps, success rate, failure rate, prints sequence of path from input state to end for first three configurations.
n = int(input("Enter the number of queens on the board : " ))
run_number_of_times = int(input("Number of times to be run: "))

while_counter = 0
sucess_steps = []
failure_steps = []
while while_counter < run_number_of_times:
   initial_state = initial_queen_positions(n)
   solution = hillclimbing(initial_state)
   seq = solution[0]
   solve = solution[1]
   if while_counter<3:
       print("Path for %s as input  is :  "%(str(initial_state)))
       for path in seq:
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
print("failure_percent: " +str((len(failure_steps)*100/run_number_of_times)))
print("success_percent: " +str((len(sucess_steps)*100/run_number_of_times)))

