import time
class QuestionDeck:
    def __init__(self):
        self.question = [
            "Find the sum of 1 + 3 + 5 + ... + 37 + 39.",
            "2P + 5 + 4P = 3P + 23, find P.",
            "Andy bought 6 dozens of pack of chips, each pack costs $15. How much money did he spend?",
            "How many factors does 36 have?",
            "The LCM and HCF of two number is 5 and 60, respectively. If one of the number is 20, what is the other number?",
            "From 15 to 40, how many numbers have 2 or 5 as a factor?",
            "In an isoceles triangle, the vertex is 80 degrees. What is the size of the angle at the base?",
            "24 is 8 percent of x, find x.",
            "Find the value of MCDLXIX."
        ]
        self.answer = ["400","6","1080","9","15","16","50","400","1469"]

class Answer:
    def __init__(self,answer,usertime):
        self.useranswer = answer
        self.time = time.time() - usertime

class Result:
    def __init__(self):        
        self.score = 0
    def calculateResult(self,user):
        correctdeck = QuestionDeck().answer
        for i in range(len(correctdeck)):
            answer = user.useranswer[i]
            correct = correctdeck[i]
            if answer == correct:
                self.score += 1
        if ((0 <= self.score <= 3) or (user.time > 1020)):
            tier = "3"
        elif ((self.score <= 6) or (user.time > 900)):
            tier = "2"
        else:
            tier = "1"
        return tier