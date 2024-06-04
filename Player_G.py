# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:11:55 2024

@author: zefin
"""

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import json
from Player import *


class Player_G(Player):
        
    def __init__(self):
        super().__init__(self)
        self.concept = None
        # self.player_setup(self.player_type, self.model)
        # self.template = self.load_template_from_config()
        
            
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