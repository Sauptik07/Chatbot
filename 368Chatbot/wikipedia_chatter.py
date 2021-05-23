from interfaces import Chatter
import wikipedia

class WikipediaChatter(Chatter):

    def __init__(self) -> None:
        super().__init__()
                
    def get_answer(self, question: str) -> str:

        answer = wikipedia.summary(question)
        return answer

        # if answer is not None and answer != "":
        #     return answer

        # return None

    
