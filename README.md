# Chatbot

<img width="471" alt="Screen Shot 2021-05-21 at 3 41 18 PM" src="https://user-images.githubusercontent.com/47649258/119190173-0094d700-ba4b-11eb-8919-67bb027926f3.png">

This chatbot is for the academia sector to help students ask course related questions and escalate problems accordingly.

This uses Piazza and wikipidia API to pull information from specific classes and provide answers accordingly.

<img width="1088" alt="Screen Shot 2021-05-21 at 3 42 20 PM" src="https://user-images.githubusercontent.com/47649258/119190307-2b7f2b00-ba4b-11eb-8538-fb999a60bef0.png">


There is also a semantic similarity and student mood indicator to populate databases with information that can be used by instructors to improve courses.

Resource for text2emotion: https://towardsdatascience.com/text2emotion-python-package-to-detect-emotions-from-textual-data-b2e7b7ce1153

The bot also takes feedback and stores them into an array and prints them in the end to show counters for negative and positive feedback.

The chatbot initially breaks down the post search into three different question segments: Module Specific, Student Specific and Administrative.

**Module Specific (all these questions will be checked for emotion analysis at the back end and a single emotion score will be preserved at the end of the survey)**:

- Was the module taught this week was presented in a sequence that helped your learning? 
  - if no, ask if s/he needs to connect to TA for a one-one session or would elaborate on what is the difficulty that the student faced? The chatbot should also provide next available Office hours in the week/contact details of TA. 
Chatbot should also provide an option for repeating the information if requested. 

If yes, go to next.

-Did you have a chance to practice?  
If not, ask 3
-if yes, what do you think, helped you most? Slides/ref text/sample code/homework/homework solutions/office hours discussions/class discussions etc.
Based on each student’s feedback, upvote the corresponding item

- Do you think that you have enough materials to practice and prepare for this module? 
  If no, ask:  would you want me to find some references for you. We can assume that there would be some list of references available for each module, which will be in a static repository (say UBLearn) and chatbot may be hardcoded with the link.

  if yes, what do you think, helped you most? Slides/ref text/sample code/homework/homework solutions/office hours discussions/class discussions etc.
	Based on each student’s feedback, upvote the corresponding item

- Was there any material that you found difficult ?
  If yes, find out more about the materials by a multiple choice answer: Slides/sample code/homework/homework solutions. We may also want to downvote the item. 

Any topic that you found difficult? 
If yes,  then chatbot can suggest some specific keywords ( like regression concept, derivation, or specific example discussed in class, TA’s clarification etc.) or allow student to key in some input, which can be used to searching for similar topics in Piazza. Piazza_api can crawl the posts. We can use tagwords/content keywords to retrieve a set of posts discussing the similar topics.
Chatbot would also prompt the student to use ‘VTA’ main menu TAB to get some questions answered, if that is immediate requirement. (VTA tab will implement the feedbackweightedlearning code to answer some topic specific doubts for each module.). Student can press the back button to come back to the main menu, or the chatbot may leave some option to come back to the main menu.

**Student specific questions**

How many class (or section) sessions did you attend?

Answer may be just preserved in a database. If the student has missed some class, Chatbot can recommend the class recording or the slides discussed in the class, just by sending the corresponding link.

On average, how many hours per week have you spent on this course (or section), including attending classes, doing readings, reviewing notes, and any other course-related work?
Answer may be just preserved in a database. If the student has not spent average acceptable hours, Chatbot may make some recommendation saying: good/need to do more/immediate attention is required. 
Chatbot can ask some personal questions like if everything is good at their end, anything is bothering them. Chatbot would directly prompt to take the  mental health survey another main menu TAB. Reference for multiple choice questions: http://d3mcbia3evjswv.cloudfront.net/files/Self-Assessment%20Form.pdf 

Did you finish your quiz this week?
If no, send the link to the quiz, which will anyway have solutions available if the due date is passed

Did you finish your discussion forum submission this week?
If no, send the link, which will anyway have posts visible to students after the due date. Student can atleast go through the topics to enhance their learning.

How satisfied were you with your effort in this course (or section)? 
Get a rating in a standard scale

what do you consider to be the topic that you understood the best in this module? 
Chatbot may provide a set of topics or tag words retrieved from Piazza for the student to choose from. Answer may be preserved in a list of Popular topics (denote it as P), where each entry will be a tuple (s, t) with s representing the student code and t representing the topic code.

what you consider to be the topic that you understood the least in this module?

Answer may be preserved in a list of Difficult topics (denote it as D), where each entry will be a tuple (s, t) with s representing the student code and t representing the topic code.
Search for the entry in P and recommend the student to connect to their peers, by making some recommendations on students’ names who would love to participate in peer discussion and have mastered the topic



**Administrative:**
Was the quiz for this week published yet?

Send the link to quiz.


When is the weekly quiz due?
Lets assume such details are available in a document and just retrieve the detail to send.

Similarly for HW/PA/ Midterm and final

Learning Objectives
What was your learning objective in the  module?
Learning concepts, b) Employing your learning to implement and analyze context, c) Application of concepts in realworld, d) Both 1, 2, e). All of 1, 2,3  

How effective it was to improve your problem solving skill?
Check for negative emotions in the comment and if it is negative ask for feedback on what to improve. If there is a positive emotions then ask for recommendations on what helped the most :  Slides/ref text/sample code/homework/homework solutions/office hours discussions/class discussions etc.
Based on each student’s feedback, upvote the corresponding item ( if it has already not been upvoted by the same student)

How effective it was to raise your confidence to do more advanced work in the subject
Check for negative emotions in the comment and if it is negative ask for feedback on what to improve. If there is a positive emotions then ask for recommendations on what helped the most :  Slides/ref text/sample code/homework/homework solutions/office hours discussions/class discussions etc.
Based on each student’s feedback, upvote the corresponding item( if it has already not been upvoted by the same student)

The course developed my ability to think critically about the subject
Check for negative emotions in the comment and if it is negative ask for feedback on what to improve. If there is a positive emotions then ask for recommendations on what helped the most :  Slides/ref text/sample code/homework/homework solutions/office hours discussions/class discussions etc.
Based on each student’s feedback, upvote the corresponding item( if it has already not been upvoted by the same student)
