from abc import ABCMeta, abstractmethod

class Chatter(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'attend') and 
                callable(subclass.attend) or 
                NotImplemented)

    @abstractmethod
    def get_answer(self, question: str) -> str:
        """Retuns a response aginst the request"""
        raise NotImplementedError
