
class question():
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def checkanswer (self,answer):
        return self.answer == answer



class quiz():
    def __init__ (self,questions):
        self.questions=questions
        self.score=0
        self.startindex=0

    def getquestion(self):
        return self.questions[self.startindex]

    def displayquestion(self):
        question=self.getquestion()
        print(f"soru {self.startindex + 1}:{question.text} ")
        for i in question.choices:
            print("-",i)

        answer = input("cevabınız:")
        self.guess(answer)
        self.loadquestion()

    def guess(self,answer):
        guestion = self.getquestion()

        if question.checkanswer(answer):
            self.score +=1
        self.startindex +=1
        

    def loadquestion(self):
        if len(self.questions) == self.startindex:
            self.showscore()
        
        else:
            self.displayprogress()
            self.displayquestion()
            
    def showscore(self):
        print (f"skorunuz :{self.score} ")

    def displayprogress(self):
        totalquestion = len(self.questions)
        number_of_question = self.startindex +1
        if number_of_question > totalquestion:
            print("game is over")
        
        else:
            print (f"question {self.startindex + 1} of {len(self.questions)}".center(100,"*"))


q1=question("en iyi programlama dili hangisidir?",["java","python","javascript","c#","react"],"python")
q2=question("en popüler programlama dili hangisidir?",["java","c#","react"],"javascript")
q3=question("en çok kazandıran programlama dili hangisidir?",["java","javascript","c#","react","python"],"c#")
q4=question("en çok kazandıran programlama dili hangisidir?",["java","javascript","c#","react","python"],"c#")
q5=question("en çok kazandıran programlama dili hangisidir?",["java","javascript","c#","react","python"],"c#")


listeq=[q1,q2,q3,q4,q5]


quiz = quiz(listeq)
question=quiz.getquestion()
print( quiz.loadquestion() )







