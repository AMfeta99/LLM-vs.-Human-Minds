
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

class Game:
    def __init__(self, model1, model2, rounds=3, questions=20):
        self.model1 = model1
        self.model2 = model2
        self.rounds = rounds
        self.questions = questions

    def start(self):
        players = {
            "0": {
                "player": Player(model=self.model1),
                "score": 0,
            },
            "1": {
                "player": Player(model=self.model2),
                "score": 0,
            },
        }

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