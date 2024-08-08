
"""
@author: Ana Maria Sousa                                               
@datum: 08/2024

@Description
Statement of Class "Game". 
The Game class manages the overall flow of the game, determining which player 
should take action at each stage.

The Game class supports two modes:
    -LLM vs. LLM: Both players are language models. In this mode, all elements 
    of the game are fully visible, allowing users to observe the gameplay and 
    analyze the interaction between the models.
    
    -LLM vs. Human: A human player competes against an LLM. In this mode, the 
    target role or word is hidden from the human player to ensure a fair 
    challenge against the virtual opponent.

In both modes, the Game class tracks the score and history of the game. It also 
provides necessary prompts and instructions to the players as needed.

"""
import random
from Player import *

class Game:
    def __init__(self, player_list, game_mode, rounds=2, questions=5):
        """
        Initialize the Game class with players, game mode, number of rounds, and questions per round.

        Parameters
        ----------
        player_list : list
            A list of player objects participating in the game.
        game_mode : str
            The mode of the game, such as 'LLM vs LLM' or 'LLM vs Human'.
        rounds : int, optional
            The number of rounds to be played in the game. The default is 2.
        questions : int, optional
            The number of questions per round. The default is 5.

        Returns
        -------
        None.
        """
        
        self.player_list = player_list
        self.game_mode=game_mode
        self.rounds = rounds
        self.questions = questions



    def start_AI_H(self):
        """
        Manages and tracks the gameplay, including rounds, player actions, and scores.
    
        This method handles the flow of Human vs LLM game. The method also prints the game 
        summary, tracks scores, and updates  players after each round.
    
        Raises
        ------
        TypeError
            Raised if an unsupported player type is encountered.
    
        Returns
        -------
        None
        """
            
        players = {}
        # Assuming players is a list containing player objects
        template = (self.player_list[0]).template 
        # Now you can use the template attribute as needed
        print(template["Game_summary"].format(questions=self.questions, rounds=self.rounds))
            
        for i, player in enumerate(self.player_list):
            players[str(i)] = {
                "player": player,
                "score": 0
            }
       
         
        print(players)   
        host_index = 0
        print_b=True
        for round in range(self.rounds):
            print(f"\nRound {round + 1}. Player {host_index + 1} is the host.")
    
            player_index = 1 - host_index
            host_player = players[str(host_index)]["player"]
            guessing_player = players[str(player_index)]["player"]
    
            # Determine which method to use based on the class of the guessing player
            if isinstance(guessing_player, Player_G):
                guessed_correctly = self._play(host_player, guessing_player)
            elif isinstance(guessing_player, Player_P):
                guessed_correctly = self._play_Pattern(host_player, guessing_player)
            elif isinstance(guessing_player, Player_I):
                extra_player = players[str(2)]["player"]
                guessed_correctly = self._play_Impostor(host_player, guessing_player, extra_player)
            else:
                raise TypeError("Unsupported player type")
    
            if guessed_correctly:
                print(f"Player {player_index + 1} guessed correctly.")
                players[str(player_index)]["score"] += 1
            else:
                print(f"Player {player_index + 1} didn't guess correctly.")
                players[str(host_index)]["score"] += 1
    
            host_index = 1 - host_index
            if round==1:
                print_b=False

        print("Final score:")
        for player_id in ['0', '1']:
            print(f"Player {int(player_id) + 1}: {players[player_id]['score']}")


            
    def start_AI(self):
        """
        Manages and tracks the gameplay, including rounds, player actions, and scores.
    
        This method handles the flow of LLM vs LLM game. The method also prints the game 
        summary, tracks scores, and updates  players after each round.
    
        Raises
        ------
        TypeError
            Raised if an unsupported player type is encountered.
    
        Returns
        -------
        None
        """
        players = {}
        for i, player in enumerate(self.player_list):
            players[str(i)] = {
                "player": player,
                "score": 0
            }
    
        print(players)
        host_index = 0
    
        for round in range(self.rounds):
            print(f"\nRound {round + 1}. Player {host_index + 1} is the host.")
    
            player_index = 1 - host_index
            host_player = players[str(host_index)]["player"]
            guessing_player = players[str(player_index)]["player"]
            
    
            # Determine which method to use based on the class of the guessing player
            if isinstance(guessing_player, Player_G):
                guessed_correctly = self._play(host_player, guessing_player)
            elif isinstance(guessing_player, Player_P):
                guessed_correctly = self._play_Pattern(host_player, guessing_player)
            elif isinstance(guessing_player, Player_I):
                extra_player = players[str(2)]["player"]
                guessed_correctly = self._play_Impostor(host_player, guessing_player, extra_player)
            else:
                raise TypeError("Unsupported player type")
    
            if guessed_correctly:
                print(f"Player {player_index + 1} guessed correctly.")
                players[str(player_index)]["score"] += 1
            else:
                print(f"Player {player_index + 1} didn't guess correctly.")
                players[str(host_index)]["score"] += 1
    
            host_index = 1 - host_index
    
        print("Final score:")
        for player_id in ['0', '1']:
            print(f"Player {int(player_id) + 1}: {players[player_id]['score']}")
    

            
    def _play(self, host, player, print_b=False):
        """
        Conducts a round of the guessing game between a host and a player.
    
        In this method, the host presents a concept, and the player asks a 
        series of questions to guess the concept. The host provides answers, 
        and the game continues until either the concept is guessed 
        correctly or the questions are exhausted.
    
        Parameters
        ----------
        host : Host
            The player acting as the host, responsible for providing the 
            concept and answering questions.
        player : Player
            The player attempting to guess the concept by asking questions.
        print_b : bool, optional
            A flag indicating whether to print additional details about the 
            game. The default is False.
    
        Returns
        -------
        bool
            Returns True if the player correctly guesses the concept during 
            the round; otherwise, returns False.
        """
        host.initialize_host(print_b)
        player.initialize_player()
        if self.game_mode==0:
            print(f"Concept: {host.concept}")
        for question_index in range(self.questions):
            question = player.ask(self.questions - question_index, print_b)
            answer = host.answer(question, print_b)

            print(f"Question {question_index + 1}: {question}. Answer: {answer}")

            player.add_observation(question, answer)

            
            if "guessed" in answer.lower():
                print(f"The Concept was {host.concept} ")
                player.add_history(host.concept)
                return True

        print(f"The Concept was {host.concept} ")
        player.add_history(host.concept)
        return False
    
    
    
    def _play_Pattern(self, host, player, print_b=False):
        """
        Conducts a round of the pattern puzzle game between a host and a player.
    
        In this game, the host presents a set of words following a specific 
        pattern/rule, and the player tries to guess the underlying rule by 
        asking questions. The game continues until the player either guesses 
        the rule correctly or the allowed number of guesses is exhausted.
    
        Parameters
        ----------
        host : Host
            The player acting as the host, responsible for providing words that 
            follow a specific pattern or rule.
        player : Player
            The player attempting to guess the rule by asking questions.
        print_b : bool, optional
            A flag indicating whether to print additional details about the 
            game. The default is False.
    
        Returns
        -------
        bool
            Returns True if the player correctly guesses the rule during the 
            round; otherwise, returns False.
        """
        host.initialize_host(print_b)
        
        for i in range(2):
            host.get_new_word_host(print_b)
        
        player.initialize_player()
        if self.game_mode==0:
            print(f"Rule: {host.rule}")
        for question_index in range(self.questions):
            print(f"The words are {host.set_objects} ")
            question = player.ask(print_b)
            answer = host.answer(question, print_b)

            print(f"Guess {question_index + 1}: {question}. Answer: {answer}")

            player.add_observation(question, answer)
            host.get_new_word_host(print_b)
            
            if "guessed" in answer.lower():
                print(f"The rule was {host.rule} ")
                player.add_history(host.rule)
                return True

        print(f"The rule was {host.rule} ")
        player.add_history(host.rule)
        return False
    
    
    def _play_Impostor(self, host, player1, player2, print_b=False):
        """
        Conducts a round of the impostor game, where players must identify the 
        impostor among them.
    
        In this game , one player is randomly assigned the role of the impostor 
        (or "spy"), while the other player knows the correct concept. 
        Both players answer questions posed by the host, and the goal is to 
        identify the impostor based on their answers. The game concludes when 
        the host votes on who they believe the impostor is.
    
        Parameters
        ----------
        host : Host
            The player acting as the host, responsible for asking questions and 
            voting to identify the impostor.
        player1 : Player
            The first player, who may either be the impostor or know the 
            correct concept.
        player2 : Player
            The second player, who may either be the impostor or know the 
            correct concept.
        print_b : bool, optional
            A flag indicating whether to print additional details about the 
            game. The default is False.
    
        Returns
        -------
        bool
            Returns True if the host correctly identifies the impostor based 
            on the players' answers; otherwise, returns False.
        """
        host.initialize_host(print_b)
        player1.initialize_player()
        
        if self.game_mode==0:
            print(f"Concept: {host.concept}")
        random_spy = random.choice([1, 2])
        if random_spy==1:
            player1.set_concept('spy')
            player2.set_concept( host.concept)
        else:
            player1.set_concept( host.concept)
            player2.set_concept('spy')
        print(f"Player { random_spy } is the spy")
            

            
        for question_index in range(self.questions):
            question = host.ask(self.questions - question_index, print_b)
            
            answer1 = player1.answer(question, print_b)
            answer2 = player2.answer(question, print_b) 

            
            print(f"Question {question_index + 1}: {question}. Player 1 answer: {answer1}. Player 2 answer: {answer2}")

            host.add_observation(question, answer1, answer2)
            player1.add_other_players_aws_spy(question, answer2)
            player2.add_other_players_aws_spy(question, answer1)
            # print(f"votes: {host.votes}")
            

        print(f"The concept was {host.concept} ")
        host.host_vote_impostor(print_b)
        print(f"votes: {host.votes}")
        print(random_spy)
        
        player1.add_history(host.concept)
        if any(str(random_spy) in vote for vote in host.votes):
            return True
        return False
    