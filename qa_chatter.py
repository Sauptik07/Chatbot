from typing import List
from interfaces import Chatter
import csv
import spacy

nlp = spacy.load('en_core_web_lg')
SIMILARITY_THRESHOLD = 0.95

class QA:

    def __init__(self, question:str, answer:str) -> None:
        self.question = question
        self.answer = answer
        self.nlp = nlp(question)

class QASet:

    def __init__(self) -> None:
        self.store = []

    # Adds a QnA item to the list
    def add(self, question:str, answer:str) -> None: 
        self.store.append(QA(question,answer))

    # Finds a QnA that has a question similar to the one asked
    def find_similar(self, question: str) -> QA:

        match = nlp(question)
        
        for qa in self.store:
            # Match similarity of a preset to question
            if qa.nlp.similarity(match) > SIMILARITY_THRESHOLD:
                return qa

        return None



class QnAChatter(Chatter):

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.qa_set = QASet()
        self.init_qna_list(filename)
        

    # Reads the content of the specified file and loads it into memory
    def init_qna_list(self, filename: str) -> None:
        with open(filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                # TODO Harden so that no errors are thrown when values are absent
                self.qa_set.add(row[0].strip(), row[1].strip())

    
    def get_answer(self, question: str) -> str:
        
        q = self.qa_set.find_similar(question)
        if q is not None:
            return q.answer

        return None