from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# write a FOR loop to iterate over the question_data
# create a Question object from each entry in question_data
# append each Question object to the question_bank

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(q_text = question_text, q_answer = question_answer)
    question_bank.append(new_question)

# bring up one of questions
# ask the user to answer the question

quiz = QuizBrain(question_bank)
quiz.next_question()

# if quiz still has questions remaining
while quiz.still_has_question():
    quiz.next_question()

print('You have completed the quiz!!!')
print(f'Your final score is: {quiz.score} / 12')
