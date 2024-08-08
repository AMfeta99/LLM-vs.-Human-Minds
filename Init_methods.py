
"""
@author: Ana Maria Sousa                                               
@datum: 08/2024

@Description
This script provides methods for configuring the game, including:
    - Getting the Selected Option: Retrieves the user's selected option from the available choices.
    - Initializing the Player: Sets up the player based on the selected game option, player type, and optional model.

"""

from Player import *

def select_option(option_dict, string_input, str_object):
    """
    Method to select the type of game and option based on input strings.
    
    Parameters
    ----------
    option_dict : dict
        A dictionary containing the available options where keys are integers and values are option names.
    string_input : str
        String to display when asking the user for input.
    str_object : str
        A descriptive string for the type of options being presented (e.g., "game", "model").
    
    Returns
    -------
    game_option : int
        The integer key corresponding to the selected option from the option_dict.
    selected_option : str
        The name of the selected option from the option_dict, or None if an invalid option was selected.
    """
    
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

def initialize_player(game_option, player_type='llm', model=None):
    """
    Initialize a player based on the selected game option, player type, and optional model.
    
    Parameters
    ----------
    game_option : int
        The selected game option that determines the type of player to initialize.
    player_type : str, optional
        The type of player to initialize (e.g., 'llm' for language learning model). The default is 'llm'.
    model : ollama object, optional
        ollama model to be used by the player. The default is None.
    
    Returns
    -------
    PlayerClass
        An instance of the player class corresponding to the selected game option.
    """
    Player_op = {0: Player_G, 1: Player_P, 2: Player_I}
    PlayerClass = Player_op[game_option]
    return PlayerClass(game_option, player_type, model)