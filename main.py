
from json import load
from quiz import Quiz

path = 'questions.json'

with open(path, 'r', encoding='utf-8') as file:
    questions = load(file)

Quiz(questions, player="quizen").play()
