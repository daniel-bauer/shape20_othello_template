#!/usr/bin/env python3
# -*- coding: utf-8 -*
#Aight. How do yall wanna divide the work? I'll be honest: I will probably not do incredibly well on the most recent shit so if you (Kyle and Justin) wanna work alone, lmk
#I think I might have done the minimax already but I dont know how to test it
#We could try doing everything else rn and then testing if it works
#Also, there are a lot of parts to the minimax problem. Like each of the "Nodes". On top of that, we have to do A/B pruning
#SHould I copy paste what i did
#For now, sure
#You should be able to play it now I dont know if it works tho
"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to  
complete and submit. 

@author: YOUR NAME AND UNI 
"""

import random
import sys
import time

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    if color == 1:
      return get_score(board)[0] - get_score(board)[1]
    return get_score(board)[1] - get_score(board)[0]


############ MINIMAX ###############################

def minimax_min_node(board, color):
  """
  Evaluates min node and returns a utility.
  """
  opp_color = 1 if color == 2 else 2

  min_utility = float("inf")

  for move in get_possible_moves(board, opp_color):

    if get_possible_moves(play_move(board, opp_color, move[0], move[1]), color):
      utility = minimax_max_node(play_move(board, opp_color, move[0], move[1]), color)
    else:
      utility = compute_utility(board, opp_color)

    if utility < min_utility:
      min_utility = utility

  return min_utility


def minimax_max_node(board, color):
  """
  Evaluate max node and return utility. 
  """
  max_utility = float("-inf")

  for move in get_possible_moves(board, color):

    if get_possible_moves(play_move(board, color, move[0], move[1]), 3 - color):
      utility = minimax_min_node(play_move(board, color, move[0], move[1]), color)
    else:
      utility = compute_utility(board, color)

    if utility > max_utility:
      max_utility = utility
  
  return max_utility
    
def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """

    max_utility = float("-inf")
    best_move = None

    for move in get_possible_moves(board, color):
      i,j = move
      new_board = play_move(board, color, i,j)
      utility = minimax_min_node(new_board, color)
      # select the move that gives the highest utility
      
      if utility > max_utility:
        max_utility = utility
        best_move = (i, j)

    return best_move # returns a move, NOT the best utility. 
    
############ ALPHA-BETA PRUNING #####################

def alphabeta_min_node(board, color, alpha, level, limit):
#def alphabeta_min_node(board, color, alpha): 

    
    if level >= limit: 
      return heuristic_evaluation(board, color)

    #...
    #  alphabeta_max_node(board, color, beta, level+1, #limit)
    return None


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, beta):
    return None


def select_move_alphabeta(board, color): 
    return 0,0 


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Minimax AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            movei, movej = select_move_minimax(board, color)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
