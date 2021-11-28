from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from project_class import QuestionDeck, Answer, Result
import time

app = Flask('Personal Math')

#home page (menu bar, start test)
class Home(MethodView):
    def get(self):
        return render_template('home.html')

#test page (questions, inputs)
class TestPage(MethodView):
    def get(self):
        math_test = Test()
        return render_template('test.html', mathtest=math_test)

#result page (user's tier, link to learning)
class ResultPage(MethodView):
    def post(self):
        test = Test(request.form)
        answer = [test.q1.data,test.q2.data,test.q3.data,test.q4.data,test.q5.data,test.q6.data,test.q7.data,test.q8.data,test.q9.data]
        user = Answer(answer,test.starttime)
        result = Result()
        _result = result.calculateResult(user)

        return render_template('result.html', outcome = _result)

#test form(import from class)
class Test(Form):
    starttime = time.time()

    q1 = StringField(QuestionDeck().question[0])
    q2 = StringField(QuestionDeck().question[1])
    q3 = StringField(QuestionDeck().question[2])
    q4 = StringField(QuestionDeck().question[3])
    q5 = StringField(QuestionDeck().question[4])
    q6 = StringField(QuestionDeck().question[5])
    q7 = StringField(QuestionDeck().question[6])
    q8 = StringField(QuestionDeck().question[7])
    q9 = StringField(QuestionDeck().question[8])

    button = SubmitField("Submit")

#class learning page (estimated time for each topic)
class LearningPage(MethodView):
    def get(self):
        return render_template('learning.html')

app.add_url_rule('/', view_func=Home.as_view('home_page'))
app.add_url_rule('/test', view_func=TestPage.as_view('test_page'))
app.add_url_rule('/result', view_func=ResultPage.as_view('result_page'))
app.add_url_rule('/learning', view_func=LearningPage.as_view('learning_page'))
app.run()