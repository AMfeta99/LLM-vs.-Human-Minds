
"""
@author: Ana Maria Sousa                                               
@datum: 05/2024

@Description
Statement of Class "Game". The Game computes ....
"""

class Game:
    def __init__(self, option):
        self.option = option
        self.name = []


    def setup_game(self):
        if self.option == 0:
            self.name='Guessing Game'
        elif self.option == 1:
            self.name='Who is Lying?'

