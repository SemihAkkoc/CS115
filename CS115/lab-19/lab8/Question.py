class Question:
    def __init__(self, question, answer, score):
        self.__questionText = question
        self.__correctAnswer = answer
        self.__score = int(score)
        self.__studentAnswer = None

    def getQuestion(self):
        return self.__questionText

    def getScore(self):
        return self.__score

    def getCorrectAnswer(self):
        return self.__correctAnswer

    def getStudentAnswer(self):
        return self.__studentAnswer

    def setQuestion(self, question):
        self.__questionText = question

    def setAnswer(self, answer):
        self.__correctAnswer = answer

    def setScore(self, score):
        self.__score = int(score)

    def isCorrectAnswer(self):
        if self.__studentAnswer == self.__correctAnswer:
            return True
        return False

    def answerQuestion(self, stuAnswer):
        self.__studentAnswer = stuAnswer


    def scoreQuestion(self):
        if self.__studentAnswer == self.__correctAnswer:
            return self.__score
        return 0

    def displayQuestion(self):
        print(self.getQuestion())

    def __repr__(self):
        return self.__questionText + '\nYour Answer:' + str(self.__studentAnswer) + '\nCorrect Answer:' + self.__correctAnswer
