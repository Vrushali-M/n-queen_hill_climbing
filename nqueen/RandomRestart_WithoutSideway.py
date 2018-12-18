import CommonFunctions
from copy import deepcopy

no_of_starts =0
no_of_steps =0
restart =[]
steps =[]

def best_move(current_state,next_queen_positions_set,current_threat):
   #returns neighbor with least heuristic if heuristic is less than current heuristic
   #returns empty set if heuristic of all neighbors is more than the current heuristic
  total =  CommonFunctions.min_threat(current_state,next_queen_positions_set)
  min_of_threats = total[0]
  all_possible_moves = total[1]
  f_threats = total[2]

  if min_of_threats < current_threat:
      best_move_next = all_possible_moves[f_threats.index(min_of_threats)]

  else:
      best_move_next = []
  return  best_move_next



def RandomRestartWithoutSideways(no_of_restarts, initial_state, n):
   #Tries to solve problem without sideway moves
   #if solving fails then randomly regenerates a new state and solves again
  global no_of_starts
  global no_of_steps
  global restart
  global steps


  while no_of_restarts <100:
      current_state = deepcopy(initial_state)

      current_h = CommonFunctions.threats(current_state)

      if current_h ==0:
          #returns true when goal is achieved
          return True

      elif current_h != 0 :
           #generates the next state
          next_queen_positions_set = CommonFunctions.next_possible_queen_positions(current_state)
          no_of_steps+=1
          current_state = best_move(current_state, next_queen_positions_set,  current_h)
          if current_state ==[]:

              init_state= CommonFunctions.initial_queen_positions(n)
              current_state = CommonFunctions.initial_queen_positions(n)
              no_of_starts += 1

              RandomRestartWithoutSideways(0, current_state, n)
              return False


          return RandomRestartWithoutSideways(0, current_state,n)


  return

n = int(input("Enter the number of queens on the board : "))
repeat = int(input("Number of times to be run: "))

success =[]
fail=[]

i=0
#Repeats the loop till the specified number of times
while i !=repeat:
  mat = CommonFunctions.create_matrix(n)
  initial_state = CommonFunctions.initial_queen_positions(n)
  A = RandomRestartWithoutSideways(0,initial_state,n)


  if A ==True:
      success.append(no_of_starts)

      restart.append(no_of_starts)
      steps.append(no_of_steps)
  else :
      fail.append(no_of_starts)
      restart.append(no_of_starts)
      steps.append(no_of_steps)

  i+=1

#prints average number of steps and restarts required to reach the solution
print("Average number of restarts for hillclimbing without sideway : ",no_of_starts/repeat)

print("Average number of steps for random restart hillclimbing without sideway : ",no_of_steps/repeat)




