import json
import re
import os
from html2text import HTML2Text
from piazza_api import Piazza
# import main as em
from nltk import word_tokenize, pos_tag
import text2emotion as te




HTML_2_TEXT = HTML2Text()
HTML_2_TEXT.ignore_links = True

all_data = {}
filtered_angry_sad_fear = []

test_piazza_class_id = "kjvuky2jrzp7ch" 

EMAIL = None
PASSWORD = None
# post_ids = []
# post_numbers = []
# post_subject = []
# post_content = []

def human_mood_find(x):
    emotion_dict = te.get_emotion(x)
    return emotion_dict

if os.path.exists('credentials.json'):
    with open('credentials.json') as f:
        credentials = json.load(f)
        EMAIL = credentials.get('email', None)
        PASSWORD = credentials.get('password', None)

def main():
    piazza = Piazza()
    piazza.user_login(email=EMAIL, password=PASSWORD)
    # network_id = input("Input your course's Piazza network ID: ").strip()
    course = piazza.network(test_piazza_class_id)
    posts = course.iter_all_posts(limit=10)
    filename = input("What is the name of the file you want to write these Piazza posts to? ").strip()
    with open(filename, 'w') as f:
        for post in posts:
            # post_ids.append(post['id'])
            f.write("Post ID is: " + post['id'] + '\n')
            f.write('\n' + '----------------------------------------------' + '\n')
            # post_numbers.append(post['nr'])
            f.write("Post number is: " + str(post['nr']))
            f.write('\n' +'----------------------------------------------' + '\n')
            #history is a list of dictionaries ordered by question and then followups after. 0th index is question and context is grabbed from that.
            # post_subject.append(post['history'][0]['subject'])
            f.write("Post subject is: " + post['history'][0]['subject'])
            f.write('\n' +'----------------------------------------------' + '\n')
            # post_content.append(post['history'][0]['content'])
            post_content = post['history'][0]['content']
            post_content_as_text = HTML_2_TEXT.handle(post_content)
            post_content_as_text = post_content_as_text.replace('\n', ' ')
            post_content_as_text = post_content_as_text.replace('  ', ' ')
            post_content_as_text = post_content_as_text.strip()
            post_content_as_text = re.sub(r'!\[\]\(.*\)', '', post_content_as_text)
            f.write("Post content is: " + post_content_as_text + '\n')
            # print(post['history'][0]['content']) 
            f.write('\n' +'----------------------------------------------' + '\n')
            f.write('\n' +'----------------------------------------------' + '\n')

            all_data[str(post['nr'])] = (str(post['nr']), post['history'][0]['subject'], post_content_as_text,)

            # print(post_ids)
            # print(post_numbers)
            # print(post_subject)
            # print(post_content)
    print(all_data)

    #loop to create sentiment DS. 
    for k in all_data:
        print(type(all_data[k]))
        lst = all_data[k]
        nr = lst[0]
        title = lst[1]
        content = lst[2]
        #enter emotion analysis here
        emotion_rating = human_mood_find(content)
        print(emotion_rating) #replace 0 with function call and pass content var to func call
        Sad_rating = emotion_rating['Sad']
        Fear_rating = emotion_rating['Fear']
        Happy_rating = emotion_rating['Happy']
        Angry_rating = emotion_rating['Angry']
        Surprise_rating = emotion_rating['Surprise']

        if Sad_rating + Fear_rating + Angry_rating > Happy_rating + Surprise_rating:
            filtered_angry_sad_fear.append(lst)
    print(len(all_data), len(filtered_angry_sad_fear))




if __name__ == '__main__':
    main()



# **** run feedback weighted learning from wiki ***** 
# prepare csv files - module specific 2 or 3 columns
# similarity function to check similarity with questions. 
# run feedback wighted

# knowledge base -> piazza -> feedback wl/

# 
