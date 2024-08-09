# LLM vs. Human Minds

This repository is the result of experiments with LLMs to develop skills in prompt eng and software development using state-of-the-art LLM and popular sources/tools such as langchain, Ollama APi, Openai API.
- [Games](#Games)
- [Game Modes](#Game_modes)
- [Setup](#Setup)
- [Usage](#usage)
- [Challenges](#Challenges)
- [Repository_files](#Repository_files)
- [Acknowledgements](#Acknowledgements)
  
![image](https://github.com/AMfeta99/LLM-vs.-Human-Minds/assets/74252797/fc4107c1-d87f-41fb-9475-67dbc9b453fa)

## Games:
**1 - Guessing Game:**
   This is a two-player Game where one player (Host) thinks of a common object/concept, and the other player attempts to guess it by asking some yes/no questions. If the guesser fails, the other player earns a point. The game is played over multiple rounds, and the player with the highest score at the end wins.

**2 - Pattern Game:**
   Game where player try to identify a common rule/characteristic shared by a set of words selected by the host. The player that is guessing can ask a limited number of questions. If they fail, the host earns a point.

**3 - Impostor Game (Who is Lying?):**
   The Impostor Game challenges players to identify the spy among them. The host tries to find out who is the impostor by asking a questions about the given concept/word. If the host fails to correctly identify the 'spy', the other player earns a point. The game is played over multiple rounds, and the player with the highest score at the end is the winner.


## Game_modes
These games allow you to choose between two modes:
- LLM vs. LLM
   : Virtual players playing against each other.
- LLM vs. Human Minds
   : Allows a human to play against a virtual player.

### LLM vs. LLM
In this mode you can choose between several open source models, such as: llama3, llama2, etc..
Although these models are not prepared for these games, it is an interesting/fun way to compare models, explore their behavior and understand some of their limitations.

### LLM vs. Human Minds
"Can u guess?" This is the game that challenges Human to face LLM models in a variety of games, from guessing to association games... challenge yourself! Will you be able to win?

Who said AI is complex, difficult or scary? In fact AI can also be interesting and fun...  so just relax and exercise your brain and has fun challenging the state of the model ;)


## Setup
- Create a virtual environment and install the required packages:
  
         $ python3 -m venv .venv
         $ source .venv/bin/activate
         $ pip install -r requirements.txt
- Download models from [Ollama](https://ollama.com/)

Optionally (in case of [OpenAI API](https://openai.com/index/openai-api) )
- Create account to get your API Key
- Create a .env file with the following variable:
  
        OPENAI_API_KEY = [ENTER YOUR OPENAI API KEY HERE]

## Usage
After the installation is ready, give it a try. To get started, you will be asked to enter: 
-  Game you want to play:
  
        0: 'Guessing Game', 1: 'Pattern Puzzel Game', 2: 'Impostor Game'
   
-  Game mode:
  
        0 : 'LLM vs LLM',  1 : 'LLM vs Human'
   
-  Desired opponent virtual:

       0: 'llama2', 1: 'llama3'


### 1- In the following photos you can see an example of a guessing game in the case of:

**1.1)** LLM vs LLM mode in which the user is just watching:

![image](https://github.com/user-attachments/assets/70b1d560-86aa-4d63-9658-7b000d398bea)

**1.2)** LLM vs Human mode in which the user actually asks the question/answer and interacts with the virtual player.

![image](https://github.com/user-attachments/assets/571424ec-bc80-45bc-a386-d0310524b8c2) 


### 2- The three games have been implemented/tested, the following photos show the case of the Pattern puzzel game and the Impostor game running in LLM vs LLM mode using llama3:

**2.1)** Pattern Puzzel Game: In this round, player 1 is the host and has entered a word/category and some examples that fall into that category. Player 2 tries to guess the word, he has 4 guesses, each time he guesses the host adds a new example that follows the same category. In the end, player 2 manages to guess the word "Animal"

![image](https://github.com/user-attachments/assets/d46076c6-a222-45e2-b2af-9e78e3c9847e)

**2.2)** Impostor Game: Three LLM take fazem parte deste jogo. In this round, Player 1 is the host and has chosen the word "book." The host asks questions to the other players, who must respond with either "yes" or "no." Player 2 is the 'spy' and doesn't know the word. The 'spy' must try ti guess the correct answers to not be spotted , while Player 3 knows the word and answers truthfully. At the end of the round, the host tries to identify the spy based on the responses given by both players.

![image](https://github.com/user-attachments/assets/0ed93623-52f7-4cb0-888e-a0caa2231b5e)


## Challenges
In this section, we discuss some of the challenges and unwanted behaviors observed in LLMs while developing and testing these games. 
These insights provide a better understanding of how LLMs function and highlight their limitations. 
Identifying these challenges and weaknesses is crucial for making improvements in future releases.

- **Diversity:** Sometimes it is found that the same model when prompted in the same way, produces very similar results. For example in the llama3 guessing game case (1.1), the model often starts with the word 'book'.
  
- **Loyalty to the prompt:** It's sometimes challenging for LLM models to strictly follow prompts from configuration files (e.g., .json). For instance, even when there's only one question left and the prompt specifies, "If there's only one question left, you must make a guess or you'll lose the game," the LLM may fail to make a guess.
  
- **Reasoning:** The difficulty in reasoning and the ability to ask relevant questions must be improved.
  
- **Heterogeneous Behavior:** Different LLMs can exhibit varying behaviors when given the same prompt due to differences in their underlying architecture, training data, and fine-tuning processes.
  
Some of these issues can be mitigated by selecting the most suitable LLM model and adopting strategies that enhance the model's memory and reasoning capabilities. One possible approach is to use tools like LangGraph, use ConversationWithMemory method form langchain.memory etc...


## Repository_files
  - [requirements.txt](https://github.com/AMfeta99/LLM-vs.-Human-Minds/blob/main/requirements.txt) (text file with a list the packages used)
  - [Photos](https://github.com/AMfeta99/LLM-vs.-Human-Minds/tree/main/photos) (folder with some screenshots of the games)

Class/Method Files:

  - [Main.py](https://github.com/AMfeta99/LLM-vs.-Human-Minds/blob/main/Main.py) (Main file, initialize/configure the game, allow selection of game options)
  
  - [Init_methods.py](https://github.com/AMfeta99/LLM-vs.-Human-Minds/blob/main/Init_methods.py) (methods for game configuration)
  
  - [Player.py](https://github.com/AMfeta99/LLM-vs.-Human-Minds/blob/main/Player.py) (Player class, implements player's roles, actions, and prompts to perform while playing)
  
  - [Game.py](https://github.com/AMfeta99/LLM-vs.-Human-Minds/blob/main/Game.py) (Game class manages the overall flow of the game, determining which player should take action at each stage etc)

Config files containing all prompts used in each game for all actions/roles:
  - [Guessing_game.json](https://github.com/AMfeta99/LLM-vs.-Human-Minds/blob/main/Guessing_game.json)
  - [PatternPuzzle_game.json](https://github.com/AMfeta99/LLM-vs.-Human-Minds/blob/main/PatternPuzzle_game.json)
  - [Impostor_game.json](https://github.com/AMfeta99/LLM-vs.-Human-Minds/blob/main/Impostor_game.json)


## Acknowledgements
- Santiago Valdarrama. (2024). [llm](https://github.com/svpino/llm/tree/main/guessing). GitHub, who contributed significantly to the idealization of the project.
- [Ollama](https://ollama.com/). Source of llm models.
- [OpenAi API](https://openai.com/index/openai-api/). Source of llm models.
- [Medium](https://medium.com/@GPTPlus/ai-in-human-robot-interaction-884ef04bdd88). repository img
