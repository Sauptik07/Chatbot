#from chat_backend import QnAChatter
from blog_chatter import BlogChatter



# admin_chatter = QnAChatter('admin.csv')

# for c in admin_chatter.qa_set.store:
#     print(c.question + " - " + c.answer)


# answer = admin_chatter.attend("when is the quiz due")
# print (answer)
# print('\n')


# module_chatter = QnAChatter('module.csv')

# for c in module_chatter.qa_set.store:
#     print(c.question + " - " + c.answer)


# answer = module_chatter.attend("when is the quiz due")
# print (answer)


blog_chatter = BlogChatter('kjvuky2jrzp7ch', 'sauptiks@buffalo.edu', 'Quest@123')

for b in blog_chatter.blog.store:
    print(b)


# answer = module_chatter.attend("when is the quiz due")
# print (answer)