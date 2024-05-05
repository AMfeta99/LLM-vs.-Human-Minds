"""
@author: Ana Maria Sousa                                               
@datum: 05/2024

@Description
This script implements....


"""

#______________________________ Librarys ______________________________________

from langchain_community.llms import Ollama

import argparse
import logging

# # model
# from langchain_groq import ChatGroq
# from langchain_openai.chat_models import ChatOpenAI


## Import functions?
from Player import *
from Game import *

#______________________________ Game_________________________________


def select_option(option_dict, string_input, str_object):
    
    # Printing the options for the user
    print(f"Choose {str_object} :")
    for key, value in option_dict.items():
        print(f"{key}: {value}")
    
    game_option= int(input( string_input))
    
    # Accessing the selected game from the dictionary
    selected_option = option_dict.get(game_option)
    
    if selected_option:
        print(f"You selected the '{selected_option}'.")
    else:
        print("Invalid option selected.")
        
    return game_option, selected_option
    

if __name__ =="__main__":
    
    ## Game options
    
    # Game to play
    str_object=' game'
    game_option_dict={0: 'Guessing', 1: 'Who is lying?'}
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
    str_input='Choose the LLM player :'
    _, LLM_player=select_option( LLM_option_dict, str_input, str_object)
    
    
    player_list.append(Player(model=Ollama(model=LLM_player)))
    
    if game_mode==0 or game_option==1:
        str_object=' Second LLM Player'
        str_input='Choose the second LLM player :'
        _, LLM_player_2= select_option( LLM_option_dict, str_input, str_object)
        player_list.append(Player(model=Ollama(model=LLM_player_2)))
    
    if game_mode==0 and game_option==1:
        str_object=' Third LLM Player'
        str_input='Choose the Third LLM player :'
        _, LLM_player_3= select_option( LLM_option_dict, str_input, str_object)
        player_list.append(Player(model=Ollama(model=LLM_player_3)))
            
            
    game=Game(player_list, game_mode)
    game.start()
    
    
    
    ## initialize players


# game = Game(
#     model1=Ollama(model="llama3"),
#     # model1=ChatOpenAI(model="gpt-4-turbo"),
#     model2=Ollama(model="llama3"),
#     # model2=ChatGroq(model_name="Llama3-70b-8192"),
#     rounds=7,
# )
# game.start()

# def parse_arguments():
#     """ 
#     Parse comand-line argurments for the scripts using argparse
#     return: argparse.Namespace: a namespace containing the parsed command-line arguments.

#     """

    # parser= argparse.ArgumentParser(description='LLM vs. Human minds')
    # parser.add_argument('Game mode', choices=['rock', 'paper', 'scissors']) 

#     return parser.parse_args()
# parse_arguments



