"""
@author: Ana Maria Sousa                                               
@datum: 05/2024

@Description
This script implements....


"""

#______________________________ Librarys ______________________________________

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# model
from langchain_groq import ChatGroq
from langchain_openai.chat_models import ChatOpenAI


## Import functions?
from Player import *
from Game import *

#______________________________ Game_________________________________
game = Game(
    model1=Ollama(model="llama3"),
    # model1=ChatOpenAI(model="gpt-4-turbo"),
    model2=Ollama(model="llama3"),
    # model2=ChatGroq(model_name="Llama3-70b-8192"),
    rounds=7,
)
game.start()