from TrueFalseQuestion import TrueFalseQuestion
from Question import Question


def initialize_question(filename, new_list):
    file = open(filename, 'r')
    for line in file:
        curr_question = line.split(';')
        curr_question[-1] = curr_question[-1][:-1:]

        if curr_question[0] == 'T':
            new_list.append(TrueFalseQuestion(curr_question[1], curr_question[2], curr_question[3], curr_question[4]))
        elif curr_question[0] == 'R':
            new_list.append(Question(curr_question[1], curr_question[2], curr_question[3]))


def grade_exam(questions):
    print('*'*9 + 'Grading Exam' + '*'*9)  # prints header
    total_points = 0
    for question in questions:
        if question.getCorrectAnswer() == question.getStudentAnswer():
            total_points += question.getScore()
        else:
            print('Incorrect Answer!\n' + question.getQuestion() + '\nYour Answer: ', question.getStudentAnswer(), '\nCorrect Answer: ', question.getCorrectAnswer(), '\n')
    print('\n' + '*'*9 + 'END OF GRADING' + '*'*9)
    print('Your Score: ', total_points, '/ 27')


questions = []
initialize_question('questions.txt', questions)

for question in questions:
    question.displayQuestion()
    question.answerQuestion(input('\nEnter choice: '))

grade_exam(questions)
