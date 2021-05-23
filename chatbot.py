from numpy import random
import text2emotion as te
from textblob import TextBlob
from nltk import word_tokenize, pos_tag
import fetch_piazza_posts
import spacy
from spacy.lang.en import English
from fetch_piazza_posts import all_data
import csv
import wikipedia

nlp = spacy.load('en_core_web_m')
print("What kind of question do you have: Admin, Module, Other")
question_type = input()
unanswered = []
similar = []

def human_mood_find(x):
    emotion_dict = te.get_emotion(x)
    return emotion_dict

print("How are you feeling?")
temp_mood1 = input()
human_mood1 = human_mood_find(temp_mood1)

if question_type == "Admin":
    print("Please enter your question.")
    question = input()
    with open('admin.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        flag = 0
        for row in csv_reader:
            d1 = nlp(question)
            d2 = nlp(row[0])
            print("______")
            print(d1)
            print(d2)
            print(d1.similarity(d2))
            print("______")

            
            if (d1.similarity(d2) > 0.92):
                print(row[1]) 
                flag = 1
                break
            
        if flag == 0:
            #append
            unanswered.append(question)
            #we have escalated prompt.

elif question_type == "Module":
    print("Please enter your question.")
    question = input()
    with open('module.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        flag = 0
        for row in csv_reader:
            d1 = nlp(question)
            d2 = nlp(row[0])
            
            if (d1.similarity(d2) > 0.92):
                print(row[1]) 
                flag = 1
                break
            
        if flag == 0:
            #append
            unanswered.append(question)

else:
    print("Please enter your question.")
    question = input()
    doc1 = nlp(question)
    file1 = open('test.txt', 'r')
    Lines = file1.readlines()
    for i in Lines:
        s_text = nlp(i)
        similar.append(doc1.similarity(nlp(i)))
    length = len(similar)
    for s in range(length):
        if similar[s] > 0.6: #remove it and just print top 10 matches. 
            print(similar[s])
            print(Lines[s])
            print("________________")
            if ("Post subject is:" in Lines[s]):
                print(Lines[s-2])
                print("Go to the question: " + "https://piazza.com/class/kjvuky2jrzp7ch?cid=" + Lines[s-2][16:])
            if ("Post content is:" in Lines[s]):
                print(Lines[s-4])
                print("Go to the question: " + "https://piazza.com/class/kjvuky2jrzp7ch?cid=" + Lines[s-4][16:])

        else:
            continue    
    
    
print("Did this answer your question: Yes/ No")
satisfaction = input()
if satisfaction == "Yes":
    FeedbackAnswers = {}
    print("Kindly answer the following questions for material feedback:")
    with open('StudentSpecific.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0])
            response = input()
            FeedbackAnswers[row[0]] = response
    print(FeedbackAnswers)
    with open('StudentSpecificAnswers.csv', 'w') as f:
        csv_writer = csv.writer(f)
        for key, value in FeedbackAnswers.items():
            csv_writer.writerow([key, value])

else:
    print("Please enter the title for what you want information on.")
    summary_topic = input()
    print(wikipedia.summary(summary_topic))

print("Do you still need help: Yes/ No")
more_help = input()
if more_help == "No":
    FeedbackAnswers = {}
    print("Kindly answer the following questions for material feedback:")
    with open('StudentSpecific.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0])
            response = input()
            FeedbackAnswers[row[0]] = response
    print(FeedbackAnswers)
    with open('StudentSpecificAnswers.csv', 'w') as f:
        csv_writer = csv.writer(f)
        for key, value in FeedbackAnswers.items():
            csv_writer.writerow([key, value])

else: 
    unanswered.append(question)
    print("Your question has been escalated. There are also office hours today from 2 pm - 5 pm.")

positive_feedbacks = []
negative_feedbacks = []

def feedback(x):
    feedback_polarity = TextBlob(x).sentiment.polarity
    if feedback_polarity>0:
        positive_feedbacks.append(x)
    else:
        negative_feedbacks.append(x)

print("How are you feeling?")
temp_mood2 = input()
human_mood2 = human_mood_find(temp_mood2)

print("Do you have any feedback?")
thank_you = "Thank you! Have a great rest of the day!"
feedback_user = input()
if (feedback_user == "No"):
    print(thank_you)
else:
    feedback(feedback_user)
    print('Positive_feebacks Count : {}'.format(len(positive_feedbacks)))
    print('Negative_feedback Count : {}'.format(len(negative_feedbacks)))



