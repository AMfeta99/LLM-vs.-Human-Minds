
"""
@author: Ana Maria Sousa                                               
@datum: 05/2024

@Description
Statement of Class "Game". The Game computes ....
"""

# class Game:
#     def __init__(self, option):
#         self.option = option
#         self.name = []


#     def setup_game(self):
#         if self.option == 0:
#             self.name='Guessing Game'
#         elif self.option == 1:
#             self.name='Who is Lying?'

from Player import *

class Game:
    def __init__(self, player_list, game_mode, rounds=3, questions=20):
        self.player_list = player_list
        self.game_mode=game_mode
        self.rounds = rounds
        self.questions = questions

    def start(self):
            
        players = {}
        if self.game_mode==1:
            self.player_list.append(Player(player_type='human'))
            
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
            if self._play(
                players[str(host_index)]["player"], players[str(player_index)]["player"]
            ):
                print(f"Player {player_index + 1} guessed correctly.")
                players[str(player_index)]["score"] += 1
            else:
                print(f"Player {player_index + 1} didn't guess correctly.")
                players[str(host_index)]["score"] += 1

            host_index = 1 - host_index

        print("Final score:")
        print(f"Player 1: {players['0']['score']}")
        print(f"Player 2: {players['1']['score']}")

    def _play(self, host, player):
        host.initialize_host()
        player.initialize_player()
        for question_index in range(self.questions):
            question = player.ask(self.questions - question_index)
            answer = host.answer(question)

            print(f"Question {question_index + 1}: {question}. Answer: {answer}")

            player.add_observation(question, answer)

            if "guessed" in answer.lower():
                return True

        return False