from wikipedia_chatter import WikipediaChatter
from blog_chatter import BlogChatter
from qa_chatter import QnAChatter
import PySimpleGUI as sg



def init_blog_chatter() -> BlogChatter:
    bc = BlogChatter('kjvuky2jrzp7ch', 'sauptiks@buffalo.edu', 'Quest@123')

    # for debugging purposes, print all the items in store
    for b in bc.blog.store:
        print(b)

    return bc


def init_admin_chatter() -> QnAChatter:
    ac = QnAChatter('admin.csv')

    for c in ac.qa_set.store:
        print(c.question + " - " + c.answer)

    return ac


BLOG_CHATTER = init_blog_chatter()
ADMIN_CHATTER = init_admin_chatter()
WIKIPEDIA_CHATTER = WikipediaChatter()

CHATTER = [BLOG_CHATTER, ADMIN_CHATTER, WIKIPEDIA_CHATTER]

def get_answer_from_any(question: str) -> str:
    for c in CHATTER:
        answer = c.get_answer(question)
        if answer is not None:
            return answer

    return None


text = 'Chatter: Hello! What can I help you with?\n'


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Multiline(text, key='-OUT-', size=(50,20), autoscroll=True, disabled=True)],
            [sg.Text('>>'),  sg.Input(key='-IN-'), sg.Button('Send')],
        ]

# Create the Window
window = sg.Window('Chatbot', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window
        break

    response = values['-IN-']

    text += '\nMe: ' + response + '\n'
    
    answer = get_answer_from_any(response)

    if answer is None:
        text += "\nChatter: I don't understand.\n"
    else:
        text += '\nChatter: ' + answer + '\n'

    window['-OUT-'].update(text)
    window['-IN-'].update("")
    window['-IN-'].SetFocus()

window.close()
