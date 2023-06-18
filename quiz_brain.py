# TODO: asking the questions
# TODO: checking is the answer was correct
# TODO: checking if we are the end of the quiz

# class QuizBrain
# arrtibutes: question_number = 0 and question_list
# methods: next_question()

# create a class called QuizBrain
# write an __init__() method.
# initialise the question_number to 0
# initialise the question_list to an input

# in challenge function
# retrieve the item at the current question_number brom the question_list
# use the input() function to show the user the Question text and ask for the user's answer

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number = self.question_number + 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False): ")
        self.check_answer(user_answer, current_question.answer)


# if quiz still has questions remaining
# create method called still_has_question().
# return a boolean depending on the value of question_number
# use the while loop to show the next question until the end

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score = self.score + 1
        else:
            print('that is wrong!!!')
        print(f'The correct answer is {correct_answer}')
        print(f'Your current score is {self.score} / {self.question_number}')
        print('\n')


