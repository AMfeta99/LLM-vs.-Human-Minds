
"""
@author: Ana Maria Sousa                                               
@datum: 05/2024

@Description
Statement of Class "Player". The Player computes ....
"""

class Player:
    def __init__(self, model):
        self.observations = []
        self.model = model
        self.concept = None
        self.history = []

    def initialize_host(self):
        template = """
        You are the host of a game where a player asks questions about
        a thing to guess what it is.

        Write the name of a thing. It must be a common object.
        It must be a single word. Do not write anything else. 
        Only write the name of the thing with no punctuation.

        Here is a list of things you cannot use:
        {history}
        """
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.model | StrOutputParser()

        self.concept = chain.invoke({"history": "\n".join(self.history)})
        self.history.append(self.concept)

        print(f"Concept: {self.concept}")

    def initialize_player(self):
        self.observations = []

    def ask(self, questions_left):
        template = """
        You are a player in a game where you need to ask Yes/No questions about 
        a thing and guess what it is.

        The thing is a common object. It is a single word.

        Here are the questions you have already asked:

        {observations}

        You only have {questions_left} questions left to ask. You want to guess
        in as few questions as possible. If there's only 1 question left, 
        you must make a guess or you'll lose the game. Be aggresive and try to
        guess the thing as soon as possible.

        Do not ask questions that you have already asked before.

        Only binary question are allowed. The question must be answered
        with a Yes/No.
         
        Be as concise as possible when asking a question. Do not anounce that you
        will ask the question. Do not say "Let's get started", or introduce your 
        question. Just write the question.

        Examples of good questions:

        - Is it a fruit?
        - Is it bigger than a car?
        - Is it alive?

        Examples of bad questions:

        - Can I ask a question?
        - Can you tell me more about the thing?
        - What is the thing?
        - How does the thing look like?
        """
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.model | StrOutputParser()
        return chain.invoke(
            {
                "observations": "\n".join(self.observations),
                "questions_left": questions_left,
            }
        )

    def answer(self, question):
        template = """
        You are the host of a game where a player asks questions about
        a {concept} trying to guess what it is.

        The player has asked you the following question: {question}.

        If the player guessed that the thing is "{concept}", answer with
        the word "GUESSED". If the question refers to "{concept}", answer
        with the word "GUESSED". 

        If the player didn't guessed, answer the question with a 
        simple Yes or No. Do not say anything else. Do not use any
        punctuation.
        """
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.model | StrOutputParser()
        return chain.invoke({"concept": self.concept, "question": question})

    def add_observation(self, question, answer):
        self.observations.append(f"Question: {question}. Answer: {answer}")