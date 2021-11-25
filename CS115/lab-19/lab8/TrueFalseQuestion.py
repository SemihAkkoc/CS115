from Question import Question


class TrueFalseQuestion(Question):
    def __init__(self, question, answer, score, incorrect_points):
        Question.__init__(self, question, answer, score)
        self.incorrect_points = incorrect_points

    def scoreQuestion(self):
        if self.__studentAnswer == self.__correctAnswer:
            return self.__score
        else:
            return -int(self.incorrect_points)

    def displayQuestion(self):
        print('True or False: ', self.getQuestion())