"""
@author: Ana Maria Sousa                                               
@datum: 08/2024

@Description
This main script allows users to select and play one of the following games:
    -Guessing Game: Players answer questions to guess the word
    -Pattern Puzzel Game: Players identify the common pattern, rule, or category shared by a group of words.
    -Impostor Game: Players guess/deduce which among them is the impostor or spy.

For each game is possivel to choose one of two modes:
    -LLM vs LLM: Two LLM models playing agains each other
    -LLM vs Human: Allows a human/user to play again a LLM
    
This script allows users to select the LLM (Language Learning Model) they want to play with.
Those models are loaded from 'Ollama'

"""

#______________________________ Librarys ______________________________________

from langchain_community.llms import Ollama

import argparse
import logging

# # model
# from langchain_groq import ChatGroq
# from langchain_openai.chat_models import ChatOpenAI

from Player import *
from Game import *
from Init_methods import *

    
#%% MAIN

if __name__ =="__main__":
    
    ## Game options
    # Game to play
    str_object=' game'
    game_option_dict={0: 'Guessing Game', 1: 'Pattern Puzzel Game', 2: 'Impostor Game'}
    game_str_input='Enter the number corresponding to the game you want to play:  '
    
    game_option, _=select_option(game_option_dict, game_str_input, str_object)
    
    ## Game mode
    str_object=' Game Mode'
    game_mode_dict= {0 : 'LLM vs LLM',  1 : 'LLM vs Human' }
    game_str_input='Enter the number corresponding to the Game mode you want to play:  '
    
    game_mode, _=select_option(game_mode_dict, game_str_input, str_object)
    
    
    ## Initialize players
    player_list=[]
    
    str_object='LLM Player'
    LLM_option_dict={0: 'llama2', 1: 'llama3'}
    #LLM_option_dict={0: 'llama-pro', 1: 'llama3', 2: 'gemma', 3:'phi', 4:'wizard-math'}

    str_input='Choose the LLM player : '
    _, LLM_player=select_option(LLM_option_dict, str_input, str_object)
    
    # Mapping game_option to player classes
    Player_op = {0: Player_G, 1: Player_P, 2: Player_I}
    player_type="llm"
    model = Ollama(model=LLM_player) 
    player_object = initialize_player(game_option, player_type, model)
    player_list = [initialize_player(game_option, player_type, model)]
    
    #initialize players depending of ame mode and game option that was choosen
    if game_mode==0 or game_option==2:
        str_object=' Second LLM Player'
        str_input='Choose the second LLM player : '
        _, LLM_player_2= select_option( LLM_option_dict, str_input, str_object)
        model = Ollama(model=LLM_player_2) 
        player_object = initialize_player(game_option, player_type, model)
        player_list.append(initialize_player(game_option, player_type, model))

    # only "impostor game" as 3 players, one is the impostor and the others normal players
    if game_mode==0 and game_option==2:
        str_object=' Third LLM Player'
        str_input='Choose the Third LLM player : '
        _, LLM_player_3= select_option( LLM_option_dict, str_input, str_object)
        model = Ollama(model=LLM_player_3) 
        player_object = initialize_player(game_option, player_type, model)
        player_list.append(initialize_player(game_option, player_type, model))
        
            
    # initialize game 
    game=Game(player_list, game_mode)
    
    # Start playing LLM vs LLM or Human vs LLM
    if game_mode:
        player_type="human"
        player_object = initialize_player(game_option, player_type)
        player_list.insert(0, initialize_player(game_option, player_type, model))
        game.start_AI_H()
    else:
        game.start_AI()
    


