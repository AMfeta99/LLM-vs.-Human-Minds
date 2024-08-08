
"""
@author: Ana Maria Sousa                                               
@datum: 07/2024

@Description
Statement of Class "Player". 
The Player class serves as a base for configuring players and providing them with 
methods to perform actions within the game. It defines the core functionalities 
and attributes that all players share.

The Player class has three specialized subclasses, each tailored to specific game modes:
    - Player_G: Handles players involved in guessing games. This subclass 
    includes methods for asking questions and making guesses based on provided 
    answers.
    
    - Player_P: Designed for pattern puzzle games. This subclass equips players 
    with methods to identify patterns and rules from a set of words or clues.
    
    - Player_I: Used for impostor games. This subclass provides functionalities 
    for players to interact with the host and other players, including identifying 
    and voting on the impostor.

Each subclass adjusts its methods and attributes to fit the specific 
requirements and dynamics of the chosen game mode.

"""
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json

class Player():
        
    def __init__(self, game_option, player_type='llm', model=None):
        """
        Initializes a Player instance with specified game settings and player type.

        Parameters
        ----------
        game_option : int
            The game option that determines which game configuration to use 
            (e.g., 0 for Guessing Game, 1 for Pattern Puzzle, 2 for Impostor Game).
        player_type : str, optional
            The type of player, either 'llm' (language learning model) or 
            'human'. The default is 'llm'.
        model : object, optional
            The model to be used if the player type is 'llm'. The default is None.

        Returns
        -------
        None
        """
        self.observations = []       
        self.player_type=player_type
        self.game_option=game_option 
        self.history = []            
        self.player_setup(player_type, model)   
        self.template = self.load_template_from_config()
           
    def player_setup(self, player_type, model):
        """
        Configures the player based on the specified type and model.

        Parameters
        ----------
        player_type : str
            The type of player ('llm' or 'human').
        model : object
            The model to be used if the player type is 'llm'.

        Returns
        -------
        None
        """
        if player_type=='llm':
            self.model=model
        elif player_type=='human':
            self.model=None
    
    
    # Assuming you're using JSON for config files
    def load_template_from_config(self):
        """
        Loads the game template from a configuration file based on the 
        selected game option.

        Returns
        -------
        template : dict
            The game template loaded from the corresponding JSON configuration 
            file.
        """
        if self.game_option==0:
            config_file_path="Guessing_game.json"
        elif self.game_option==1:
            config_file_path="PatternPuzzle_game.json"
        elif self.game_option==2:
            config_file_path="Impostor_game.json"

        try: 
            with open(config_file_path, 'r') as f:
                template = json.load(f)
        except json.JSONDecodeError as e:
            print("JSON decoding error:", e)
            
        return template


    def initialize_player(self):
        """
        Initializes the player by clearing previous observations.

        Returns
        -------
        None
        """
        self.observations = []

#%% Sub-classes of players  
    
class Player_G(Player):
    def __init__(self, game_option, player_type='llm', model=None):
        """
        Initialize a Player_G instance for guessing games.

        Parameters
        ----------
        game_option : int
            The game option that determines the specific game.
        player_type : str, optional
            The type of player, either 'human' or 'llm' (language learning model). The default is 'llm'.
        model : object, optional
            The model to be used if the player type is 'llm'. The default is None.

        Returns
        -------
        None
        """
        super().__init__(game_option, player_type, model)
        self.concept = None

    def initialize_host(self, print_b):
        """
        Initializes the host by setting the concept based on player type.

        Parameters
        ----------
        print_b : bool
            A flag indicating whether to print additional details about the 
            initialization. The default is False.

        Returns
        -------
        None
        """
        if self.player_type == 'human':
            if print_b:
                print(self.template["host_instruct"])

            concept = input('Enter concept: ')
            self.concept = concept
        else:
            template = self.template["host_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            self.concept = chain.invoke({"history": "\n".join(self.history)})

        self.history.append(self.concept)

    def ask(self, questions_left, print_b):
        """
        Asks a question and returns the response.

        Parameters
        ----------
        questions_left : int
            The number of questions remaining.
        print_b : bool
            A flag indicating whether to print additional details about the 
            question. The default is False.

        Returns
        -------
        str
            The question to asked.
        """
        if self.player_type == 'human':
            if print_b:
                print(self.template["ask_instruct"])
            observation = input('Enter Question: ')
            return observation
        else:
            template = self.template["ask_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke(
                {
                    "observations": "\n".join(self.observations),
                    "questions_left": questions_left,
                }
            )

    def answer(self, question, print_b):
        """
        Provides an answer to a question based on the player type.

        Parameters
        ----------
        question : str
            The question to be answered.
        print_b : bool
            A flag indicating whether to print additional details about the 
            answer. The default is False.

        Returns
        -------
        str
            The answer to the question.
        """
        if self.player_type == 'human':
            if print_b:
                print(self.template["answer_instruct"])
            print(question)
            answ = input('Is it correct? (yes/no): ')
            return answ
        else:
            template = self.template["answer_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke({"concept": self.concept, "question": question})

    def add_observation(self, question, answer):
        """
        Adds an observation to the list of observations.

        Parameters
        ----------
        question : str
            The question asked.
        answer : str
            The answer received.

        Returns
        -------
        None
        """
        self.observations.append(f"Question: {question}. Answer: {answer}")
        
    def add_history(self, new_concept):
        """
        Adds a new concept to the history.

        Parameters
        ----------
        new_concept : str
            The new concept to be added to the history.

        Returns
        -------
        None
        """
        self.history.append(new_concept)






class Player_P(Player):
    def __init__(self, game_option, player_type='llm', model=None):
        """
        Initialize a Player_P instance for pattern games.

        Parameters
        ----------
        game_option : int
            The game option that determines the specific game settings.
        player_type : str, optional
            The type of player, either 'human' or 'llm'. The default is 'llm'.
        model : object, optional
            The model to be used if the player type is 'llm'. The default is None.

        Returns
        -------
        None
        """
        super().__init__(game_option, player_type, model)
        self.rule= None ## rule that must be follow        
        self.set_objects =[] ## set of objects that follow the rule
        
    def initialize_player(self):
        """
        Initializes the player by clearing observations and set objects.

        Returns
        -------
        None
        """
        self.observations = []
        self.set_objects =[]

    def initialize_host(self, print_b):
        """
        Initializes the host by setting the rule based on player type.

        Parameters
        ----------
        print_b : bool
            A flag indicating whether to print additional details about the 
            initialization. The default is False.

        Returns
        -------
        None
        """
        if self.player_type == 'human':
            if print_b:
                print(self.template["host_instruct_rule"])

            rule = input('Enter the rule: ')
            self.rule = rule
        else:
            template = self.template["host_instruct_rule"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            self.rule = chain.invoke({"history": "\n".join(self.history)})

        self.history.append(self.rule)


    def get_new_word_host(self, print_b):
        """
        Adds a new word that follows the rule to the set of objects.

        Parameters
        ----------
        print_b : bool
            A flag indicating whether to print additional details about the 
            process. The default is False.

        Returns
        -------
        None
        """
        if self.player_type == 'human':
            if print_b:
                print(self.template["host_instruct_words"])

            word= input('Enter a word that follow the rule: ')
            self.set_objects.append(word)
        else:
            template = self.template["host_instruct_words"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            
            word=chain.invoke(
                {
                    "rule": self.rule,
                    "set_objects" : "\n".join(self.set_objects),
                }
            )
            self.set_objects.append(word)
        

    def ask(self, print_b):
        """
        Asks a guess question and returns the response.

        Parameters
        ----------
        print_b : bool
            A flag indicating whether to print additional details about the 
            question. The default is False.

        Returns
        -------
        str
            The guess question.
        """
        if self.player_type == 'human':
            if print_b:
                print(self.template["ask_instruct"])
            observation = input('Enter Guess: ')
            return observation
        else:
            template = self.template["ask_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke(
                {
                    "set_objects" : "\n".join(self.set_objects),
                    "observations": "\n".join(self.observations),
                }
            )
        

    def answer(self, question, print_b):
        """
        Provides an answer to a guess question based on player type.

        Parameters
        ----------
        question : str
            The guess question.
        print_b : bool
            A flag indicating whether to print additional details about the 
            answer. The default is False.

        Returns
        -------
        str
            The answer to the guess question, either 'GUESSED' or 'WRONG'.
        """
        
        if self.player_type == 'human':
            if print_b:
                print(self.template["answer_instruct"])
            print(question)
            answ = input('Is it correct? (GUESSED/WRONG): ')
            return answ
        else:
            template = self.template["answer_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke({"rule": self.rule,  "question": question})

    def add_observation(self, question, answer):
        """
        Adds an observation to the list of observations.

        Parameters
        ----------
        question : str
            The question asked.
        answer : str
            The answer received.

        Returns
        -------
        None
        """
        self.observations.append(f"Question: {question}. Answer: {answer}")
        
    def add_history(self, new_rule):
        """
        Adds a new rule to the history.

        Parameters
        ----------
        new_rule : str
            The new rule to be added to the history.

        Returns
        -------
        None
        """
        self.history.append(new_rule)
        

        

class Player_I(Player):
    def __init__(self, game_option, player_type='llm', model=None):
        """
        Initialize a Player_I instance for impostorgames.

        Parameters
        ----------
        game_option : int
            The game option that determines the specific game settings.
        player_type : str, optional
            The type of player, either 'human' or 'llm'. The default is 'llm'.
        model : object, optional
            The model to be used if the player type is 'llm'. The default is None.

        Returns
        -------
        None
        """
        super().__init__(game_option, player_type, model)
        self.concept = None
        self.votes = []
        self.history_questions =[]

        
    def initialize_player(self):
        """
        Initializes the player by clearing observations and question history.

        Returns
        -------
        None
        """
        self.observations = []
        self.history_questions =[]

    def initialize_host(self, print_b):
        """
        Initializes the host by setting the concept and resetting votes.

        Parameters
        ----------
        print_b : bool
            A flag indicating whether to print additional details about the 
            initialization. The default is False.

        Returns
        -------
        None
        """
        self.votes = []
        if self.player_type == 'human':
            if print_b:
                print(self.template["host_instruct"])

            concept = input('Enter concept: ')
            self.concept = concept
        else:
            template = self.template["host_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            self.concept = chain.invoke({"history": "\n".join(self.history)})

        self.history.append(self.concept)
        
    def set_concept(self, word):
        """
        Sets the concept for the player.

        Parameters
        ----------
        word : str
            The concept or role to be set for the player (e.g., 'spy').

        Returns
        -------
        None
        """
        self.concept=word
        

    def ask(self, questions_left, print_b):
        """
        Asks a question based on the player's concept and remaining questions.

        Parameters
        ----------
        questions_left : int
            The number of questions left to ask.
        print_b : bool
            A flag indicating whether to print additional details about the 
            question. The default is False.

        Returns
        -------
        str
            The question generated or input by the player.
        """
        if self.player_type == 'human':
            if print_b:
                print(self.template["ask_instruct"])
            observation = input('Enter Question: ')
            return observation
        else:
            template = self.template["ask_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke(
                {
                    "concept" : self.concept,
                    "observations": "\n".join(self.observations),
                    "questions_left": questions_left,
                }
            )

    def answer(self, question, print_b):
        """
        Provides an answer to a question based on the player's concept 
        (e.g., spy or regular player).

        Parameters
        ----------
        question : str
            The question asked.
        print_b : bool
            A flag indicating whether to print additional details about the 
            answer. The default is False.

        Returns
        -------
        str
            The answer to the question, which may vary depending on the 
            concept (e.g., 'yes'/'no' or a more detailed response).
        """
        if self.concept=='spy':
            template=self.template["answer_instruct_spy"]
        else:
            template=self.template["answer_instruct"]
            
        if self.player_type == 'human':
            if print_b:
                print(template)
            print(question)
            answ = input('Is it correct? (yes/no): ')
            return answ
        
        elif self.concept=='spy':
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke({"history_questions": "\n".join(self.history_questions),
                                 "question": question})
        else:
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke({"concept": self.concept, "question": question})
        
    def host_vote_impostor(self,  print_b):
        """
        Collects votes on who the impostor is from the host.

        Parameters
        ----------
        print_b : bool
            A flag indicating whether to print additional details about the 
            voting process. The default is False.

        Returns
        -------
        None
        """
        if self.player_type == 'human':
            if print_b:
                print(self.template["host_vote_instruct"])
            answ = input('who is the impostor? (player 1/player 2): ')
            return self.votes.append(answ)
        else:
            template = self.template["host_vote_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            # vote=chain.invoke({ "answer1": answer1, "answer2": answer2, "concept": self.concept,"question": question})
            vote=chain.invoke({ "concept": self.concept, "observations": self.observations})

            self.votes.append(vote)

    def add_observation(self, question, answer1, answer2):
        """
        Adds an observation based on the answers from two players.

        Parameters
        ----------
        question : str
            The question asked.
        answer1 : str
            The answer given by player 1.
        answer2 : str
            The answer given by player 2.

        Returns
        -------
        None
        """
        self.observations.append(f"Question: {question}  Player 1 answer: {answer1}. Player 2 answer: {answer2}")
        
    def add_other_players_aws_spy(self, question, answer):
        """
        Records answers from other players when the current player is a spy.

        Parameters
        ----------
        question : str
            The question asked.
        answer : str
            The answer given by another player.

        Returns
        -------
        None
        """
        self.history_questions.append(f"Question: {question}  Answer: {answer}")
        
    def add_history(self, new_concept):
        """
        Adds a new concept or role to the player's history.

        Parameters
        ----------
        new_concept : str
            The new concept or role to be added to the history.

        Returns
        -------
        None
        """
        self.history.append(new_concept)

