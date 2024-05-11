
"""
@author: Ana Maria Sousa                                               
@datum: 05/2024

@Description
Statement of Class "Player". The Player computes ....
"""
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import json

class Player():
        
    def __init__(self, game_option, player_type='llm', model=None):
        self.observations = []       #fica
        self.player_type=player_type #fica
        self.game_option=game_option #fica
        self.concept = None          ## player_guess
        self.history = []            ## fica
        self.player_setup(player_type, model)   ##fica
        self.template = self.load_template_from_config() ##fica
        
     ## fica        
    def player_setup(self, player_type, model):
        if player_type=='llm':
            self.model=model
        elif player_type=='human':
            self.model=None
    
    #fica
    # Assuming you're using JSON for config files
    def load_template_from_config(self):
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

            
    def initialize_host(self, print_b):
        if self.player_type=='human':
            if print_b:
                print(self.template["host_instruct"])
                
            concept=input('Enter concept: ')
            self.concept=concept
        else:
            template=self.template["host_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            self.concept = chain.invoke({"history": "\n".join(self.history)})
            
        self.history.append(self.concept)


    def initialize_player(self):
        self.observations = []

    def ask(self, questions_left, print_b):
        if self.player_type=='human':
            if print_b:
                print(self.template["ask_instruct"])
            observation=input('Enter Question: ')
            return observation
        
        else:
            template=self.template["ask_instruct"]
    
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke(
                {
                    "observations": "\n".join(self.observations),
                    "questions_left": questions_left,
                }
            )

    def answer(self, question, print_b):
        if self.player_type=='human':
            if print_b:
                print(self.template["answer_instruct"])
            print(question)
            answ=input('Is it correct? (yes/no): ')
            return answ
        
        else:
            template=self.template["answer_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke({"concept": self.concept, "question": question})

    def add_observation(self, question, answer):
        self.observations.append(f"Question: {question}. Answer: {answer}")
    

class Player_Guess(Player):
        
    def __init__(self, game_option, player_type='llm', model=None):
        super().__init__(self, game_option, player_type='llm', model=None)
        self.concept = None
        self.player_setup(player_type, model)
        self.template = self.load_template_from_config()
        
            
    def initialize_host(self, print_b):
        if self.player_type=='human':
            if print_b:
                print(self.template["host_instruct"])
                
            concept=input('Enter concept: ')
            self.concept=concept
        else:
            template=self.template["host_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            self.concept = chain.invoke({"history": "\n".join(self.history)})
            
        self.history.append(self.concept)



    def ask(self, questions_left, print_b):
        if self.player_type=='human':
            if print_b:
                print(self.template["ask_instruct"])
            observation=input('Enter Question: ')
            return observation
        
        else:
            template=self.template["ask_instruct"]
    
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke(
                {
                    "observations": "\n".join(self.observations),
                    "questions_left": questions_left,
                }
            )

    def answer(self, question, print_b):
        if self.player_type=='human':
            if print_b:
                print(self.template["answer_instruct"])
            print(question)
            answ=input('Is it correct? (yes/no): ')
            return answ
        
        else:
            template=self.template["answer_instruct"]
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.model | StrOutputParser()
            return chain.invoke({"concept": self.concept, "question": question})

    def add_observation(self, question, answer):
        self.observations.append(f"Question: {question}. Answer: {answer}")