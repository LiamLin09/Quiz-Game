# class Question
# attributes: Text and Answer
# ex: new_q = Question('2+3=5', 'True')
# new_q = Question()

# write a FOR loop to iterate over the question_data
# create a Question object from each entry in question_data
# append each Question object to the question_bank

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer



