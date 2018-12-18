import random
from copy import deepcopy
from collections import Counter

def display_board(Matrix):
   #'''It displays a n*n Matrix'''
   n = len(Matrix)
   for i in range(n):
       for j in range(n):
           print(Matrix[j][i], end='  ')
       print()
   print()

def create_matrix(n):
   #'''It creates a n * n Matrix with elements as zeros'''
  Matrix_zero = [[0 for x in range(n)] for y in range(n)]
  return Matrix_zero

def create_random_queen_placement(positions):
   #Based on Queen Positions in Columns it creates n*n matrix returns using display_board function
  n = len(positions)
  Matrix = create_matrix(n)
  for i in range(n):
      j = positions[i]
      Matrix[i][j] = "Q"
  return display_board(Matrix)

def initial_queen_positions(n):
   # It creates initial state - a set of n positions for n queens values between (0, n-1) using random.ranint
   positions = []
   for i in range(n):
       positions.append(random.randint(0,n-1))
   return positions

def threats(queen_positions_col):
   # Calculates number of threats on a board at an instance
   threats = 0
   count_queen_row = Counter()
   count_queen_dia1 = Counter()
   count_queen_dia2 = Counter()

   for row, col in enumerate(queen_positions_col):
       count_queen_row[col] = count_queen_row[col] + 1
       count_queen_dia1[row - col] = count_queen_dia1[row-col]+ 1
       count_queen_dia2[row + col] = count_queen_dia2[row + col] +1

   count_all = [count_queen_row, count_queen_dia1, count_queen_dia2]
   for count in count_all:

       for key in count:
           threats =  threats + (count[key] * (count[key] - 1)) / 2

   return threats

def next_possible_queen_positions(current_queen_positions):
   #Based on current Queen position, it generates next possible positions . Example if Q in Col 0 is 1 then its next_possible_positions [0,2,3]
   n = len(current_queen_positions)
   next_queen_positions=[]
   for i in range(n):
       next=[]
       for j in range(n):
           if j != current_queen_positions[i]:
               next.append(j)

       next_queen_positions.append(next)
   return next_queen_positions


def min_threat(current_state,next_queen_positions_set):

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

   min_of_threats = min(f_threats)
   return min_of_threats, all_possible_moves,f_threats

