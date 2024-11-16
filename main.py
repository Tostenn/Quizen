from quiz import Quiz
from json import load

path = 'data/questions.json'

with open(path, 'r', encoding='utf-8') as file:
    questions = load(file)

Quiz(questions, player="CR7").play()
