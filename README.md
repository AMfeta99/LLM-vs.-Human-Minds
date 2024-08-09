# LLM vs. Human Minds

This repository is the result of experiments with LLMs to develop skills in prompt eng and software development using state-of-the-art LLM and popular sources/tools such as langchain, Ollama APi, Openai API.

![image](https://github.com/AMfeta99/LLM-vs.-Human-Minds/assets/74252797/fc4107c1-d87f-41fb-9475-67dbc9b453fa)

# Games:
**1- Guessing Game:**
This is a two-player Game where one player (Host) thinks of a common object/concept, and the other player attempts to guess it by asking some yes/no questions. If the guesser fails, the other player earns a point. The game is played over multiple rounds, and the player with the highest score at the end wins.

**2- Pattern Game:**
Game where player try to identify a common rule/characteristic shared by a set of words selected by the host. The player that is guessing can ask a limited number of questions. If they fail, the host earns a point.

**3- Impostor Game (Who is Lying?):**
The Impostor Game challenges players to identify the spy among them. The host tries to find out who is the impostor by asking a questions about the given concept/word. If the host fails to correctly identify the 'spy', the other player earns a point. The game is played over multiple rounds, and the player with the highest score at the end is the winner.


## Game modes
These games have the option of choosing:
- LLM vs. LLM
   : Two virtual players who complement each other
- LLM vs. Human Minds
   : Allows a human to play against a virtual player.

### LLM vs. LLM
In this mode you can choose between several open source models, such as:
Although these models are not prepared for these games, it is an interesting/fun way to compare models, explore their behavior and understand some of their limitations.

(descrever algumas das falhas observadas)

### LLM vs. Human Minds
"Can u guess?" This is the game that challenges Human to face LLM models in a variety of games, from guessing to association games... challenge yourself! Will you be able to win?

Who said AI is complex, difficult and scary? In fact AI can also be interesting and fun...  so just relax and exercise your brain and has fun challenging the state of the model ;)

## Setup
- Create a virtual environment and install the required packages:
  
         $ python3 -m venv .venv
         $ source .venv/bin/activate
         $ pip install -r requirements.txt
- Download models from [Ollama](https://ollama.com/)

Optionally (in case of [OpenAI API](https://openai.com/index/openai-api)
- Create account to get your API Key
- Create a .env file with the following variable:
  
        OPENAI_API_KEY = [ENTER YOUR OPENAI API KEY HERE]



## Acknowledgements
- Santiago Valdarrama. (2024). [llm](https://github.com/svpino/llm/tree/main). GitHub, who contributed significantly to the idealization of the project.
- [Ollama](https://ollama.com/). Source of llm models.
- [OpenAi API](https://openai.com/index/openai-api/). Source of llm models.
- [Medium](https://medium.com/@GPTPlus/ai-in-human-robot-interaction-884ef04bdd88). repository img
