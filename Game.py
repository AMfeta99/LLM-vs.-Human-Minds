
"""
@author: Ana Maria Sousa                                               
@datum: 05/2024

@Description
Statement of Class "Game". The Game computes ....
"""

from Player import *

class Game:
    def __init__(self, player_list, game_mode, rounds=3, questions=2):
        self.player_list = player_list
        self.game_mode=game_mode
        self.rounds = rounds
        self.questions = questions


    def start_AI_H(self):
            
        players = {}
        if self.game_mode==1:
            game_option=(self.player_list[0]).game_option
            self.player_list.append( Player(game_option, player_type='human'))
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
            if self._play(
                players[str(host_index)]["player"], players[str(player_index)]["player"]
            ):
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
            if self._play(
                players[str(host_index)]["player"], players[str(player_index)]["player"]):
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
                return True

        print(f"The Concept was {host.concept} ")
        return False
    
    # def start(self):
            
    #     players = {}
    #     if self.game_mode==1:
    #         self.player_list.append(Player(player_type='human'))
    #         # Assuming players is a list containing player objects
    #         template = (self.player_list[0]).template 
    #         # Now you can use the template attribute as needed
    #         print(template["Game_summary"].format(questions=self.questions, rounds=self.rounds))
            
            
    #     for i, player in enumerate(self.player_list):
    #         players[str(i)] = {
    #             "player": player,
    #             "score": 0
    #         }
        
         
    #     print(players)   
    #     host_index = 0
        
    #     for round in range(self.rounds):
    #         print(f"\nRound {round + 1}. Player {host_index + 1} is the host.")

    #         player_index = 1 - host_index
    #         if self._play(
    #             players[str(host_index)]["player"], players[str(player_index)]["player"]
    #         ):
    #             print(f"Player {player_index + 1} guessed correctly.")
    #             players[str(player_index)]["score"] += 1
    #         else:
    #             print(f"Player {player_index + 1} didn't guess correctly.")
    #             players[str(host_index)]["score"] += 1

    #         host_index = 1 - host_index

    #     # print("Final score:")
    #     # print(f"Player 1: {players['0']['score']}")
    #     # print(f"Player 2: {players['1']['score']}")
    #     print("Final score:")
    #     for player_id in ['0', '1']:
    #         print(f"Player {int(player_id) + 1}: {players[player_id]['score']}")