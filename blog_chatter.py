from typing import List
from interfaces import Chatter
from chat_utils import cleanup_html
import spacy
from piazza_api import Piazza

# Global Utilities
NLP = spacy.load('en_core_web_lg')

# Constants
SIMILARITY_THRESHOLD = 0.8
POST_LIMIT = 10



class Post:

    def __init__(self, id:str, number:int, subject:str, content:str) -> None:
        self.id = id
        self.number = number
        self.subject = subject
        self.content = content
        self.nlp = NLP(subject)

    def __str__(self) -> str:
        return "ID: " + self.id + ", Number: " + str(self.number) + ", Subject: " + self.subject

class Blog:

    def __init__(self) -> None:
        self.store: List[Post] = []

    # Adds a Post item to the blog
    def add(self, post: Post) -> None: 
        self.store.append(post)

    # Finds a QnA that has a question similar to the one asked
    def find_similar(self, question: str) -> Post:

        match = NLP(question)
        
        for post in self.store:
            # Match similarity of a preset to question
            if post.nlp.similarity(match) > SIMILARITY_THRESHOLD:
                return post

        return None



class BlogChatter(Chatter):

    def __init__(self, blog_id: str, email: str, password: str) -> None:
        super().__init__()
        self.blog = Blog()
        self.blog_id = blog_id
        self.init_blog(blog_id, email, password)
        

    # Reads the content of the specified file and loads it into memory
    def init_blog(self, blog_id: str, email: str, password: str) -> None:
    
        piazza = Piazza()
        piazza.user_login(email=email, password=password)
        course = piazza.network(blog_id)
        posts = course.iter_all_posts(limit=POST_LIMIT)

        for post in posts:
            subject = post['history'][0]['subject']
            content = cleanup_html(post['history'][0]['content'])
            
            self.blog.add(Post(
                post['id'], 
                post['nr'], 
                subject, 
                content))
                
    def get_answer(self, question: str) -> str:
        
        q = self.blog.find_similar(question)
        if q is not None:
            return q.content

        return None

    
