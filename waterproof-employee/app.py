from flask import Flask, render_template, request, redirect, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
# from multiprocessing import Value
import openai
import pandas as pd
import csv
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
os.environ["OPENAI_API_KEY"] = "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"
# openai.api_key = "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"
# openai.api_key = "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"
Session(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

questions = {
    1: "How much water is there on Earth?",
    2: "How much of the all the water on the planet is fresh?",
    3: "How much water does an average home use in a day?",
    4: "What does Xylem do?",
    5: "What are the main stages in the water cycle?",
}

options = {
    1: ["70%", "40%", "90%", "10%"],
    2: ["Less than 5%", "5-10%", "10-20%", "More than 20%"],
    3: ["50 gallons", "2 gallons", "100 gallons", "1,000 gallons"],
    4: ["Water technology provider, creating innovative and smart solutions", "Yes, we use it in our workplace but I don't know much", "I have never heard about Xylem", "I don't care"],
    5: ["Evaporation, condensation, precipitation", 
        "Condensation, precipitation, irrigation",
        "Distribution, condensation, precipitation","Motion, harvestation, precipitation"],
}

facts = {
    1: "70% of the Earth's surface is covered by water.",
    2: "Nearly 97% of the world’s water is salty or otherwise undrinkable. Another 2% is locked in ice caps and glaciers. That leaves just 1% for all of humanity’s needs",
    3: "The average American uses 100 gallons of water per day.",
    4: "Xylem is a leading global water technology company committed to developing innovative technology solutions to the world’s water challenges.",
    5: "The water cycle is the continuous movement of water on, above and below the surface of the Earth. The water cycle involves the evaporation and transpiration of water from Earth's surface (including the oceans), the condensation of water vapor into water droplets, and the precipitation of water in all forms (rain, snow, sleet, hail etc.) and the return of water to Earth's surface through runoff, drainage and groundwater recharge.",
}
answers = []
i = 1

# @app.route('/', methods=['GET'])
# def welcome():
#     return render_template('home.html')
@app.route('/login', methods=['GET']) # define login page path
def login(): # define login page fucntion
        return render_template('login.html')
####################################################################
@app.route('/register', methods=['GET'])# we define the sign up path
def register(): # define the sign up function
       return render_template('register.html')

@app.route('/volunteer', methods=['GET'])# we define the sign up path
def volunteer(): # define the sign up function
       return render_template('opportunities.html')


@app.route('/stats', methods=['GET'])# we define the sign up path
def stats(): # define the sign up function
       return render_template('stats.html')

@app.route('/peerstats', methods=['GET'])# we define the sign up path
def peerstats(): # define the sign up function
       return render_template('peerstats.html')

####################################################################@auth.route('/logout') # define logout path
def logout(): #define the logout function
    return 'logout'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return redirect(url_for('onboard'))

@app.route('/onboarding', methods=['GET', 'POST'])
def onboard():
    global i
    if request.method == 'POST':
        data = request.form
        answer = data.get('answer', 'default')
        answers.append(answer)
        print(answers)
        btn_label = 'Next' if i < len(questions) else 'Submit'
        print('In POST')
        i += 1
        if i == 5:
            i = 0
            with open('./tmp/answers.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([answers])
                
            return render_template('./PurpleAdmin-Free-Admin-Template/dashboard.html')
        else:
            return render_template('./PurpleAdmin-Free-Admin-Template/onboarding.html', question_label=questions[i], button_label=btn_label)
    else:
        return render_template('onboarding.html', question_label=questions[1], button_label='Next')
        # else:
        #     data = request.form
        #     answer = data['answer']
        #     # print(answer)
        #     answers.append(answer)
        #     print(answers)
        #     btn_label = 'Next' if i < len(questions) else 'Submit'
        #     return render_template('index.html', question_label=questions[i], button_label=btn_label)


@app.route('/riddle', methods=['GET', 'POST'])
def riddle():
    global i, answers
    try:
        if request.method == 'POST':
            data = request.form
            answer = data.get('comp_select')
            # answer = data.get('answer', 'default')
            # print(answer)
            answers.append(answer)
            # print(answers)
            # btn_label = 'Next' if i < len(questions) else 'Submit'
            print('In POST')
            i += 1
            if i == 5:
                i = 0
                # with open('answers.csv', 'a', newline='') as f:
                #     writer = csv.writer(f)
                #     writer.writerow([answers])
                ans = []
                for i in options.values():
                    ans.append(i[0])
                
                score = 0
                selected_answers = answers
                for i in range(len(selected_answers)):
                    if ans[i] == selected_answers[i]:
                        score +=5

                answers = []
                    
                return render_template("quiz_thanks.html", score=score)
            else:
                data = request.form
                answer = data.get('comp_select', None)
                print(answer)
                if answer is None or i == 1:
                    fact = ''
                else:
                    fact = facts[i]

                return render_template('quiz.html', question_label=questions[i], options_label=options[i])
        else:
            return render_template('quiz.html', question_label=questions[1], options_label=options[1])

    except Exception as e:
        print(e)
        # else:
        #     data = request.form
        #     answer = data['answer']
        #     # print(answer)
        #     answers.append(answer)
        #     print(answers)
        #     btn_label = 'Next' if i < len(questions) else 'Submit'
        #     return render_template('index.html', question_label=questions[i], button_label=btn_label)

prompt_template= """

Paragraph: There is the same amount of water on Earth as there was when the Earth was formed. The water from your faucet could contain molecules that dinosaurs drank.
Question: How much water is there on Earth? Answer: The same amount as when the Earth was formed

Paragraph: Water regulates the Earth’s temperature. It also regulates the temperature of the human body, carries nutrients and oxygen to cells, cushions joints, protects organs and tissues, and removes wastes.
Question: What does water do? Answer: It regulates the Earth’s temperature

Paragraph: Nearly 97% of the world’s water is salty or otherwise undrinkable. Another 2% is locked in ice caps and glaciers. That leaves just 1% for all of humanity’s needs — all its agricultural, residential, manufacturing, community, and personal needs. Hence, water consumption is very necessary.
Question: Why is water conservation necessary? Answer: Only 1% of the world’s water is available for all of humanity’s needs — its agricultural, residential, manufacturing, community, and personal needs

Paragraph: The average total home water use for each person in the U.S. is about 50 gallons a day.
The average cost for water supplied to a home in the U.S. is about $2.00 for 1,000 gallons, which equals about 5 gallons for a penny.
Question: How much water does the average person use in a day? Answer: About 50 gallons a day 

Paragraph: According to the United Nations, an American in the United States uses 575 litres of water a day, an Italian uses 385 litres, while an Indian and a Chinese use 135 litres and 85 litres respectively. Have you ever wondered how much space is taken up by an apple or a steak? Besides our apple, we must consider the ground to cultivate the apple tree on, the wood for the crates that are used to transport the apples, the fuel for transportation, an infrastructure for collection and sale, etc. These are all activities that we do not see, but which have a great influence. If we compare the space that is occupied physically by an apple or by a steak, and what is necessary to bring these two foods to our tables, we notice that the two values are quite different. Why? In the calculation we have not only considered the space they occupy physically, but also the amount of water consumption to produce the apple, i.e. its ecological footprint.
"""

# Question: Which one takes up more space, an apple or a steak? Answer: A steak, and the reason is that it has a larger ecological footprint and in turn larger water footprint.
# custom_prompt="""
# Paragraph: Elon Musk was a born in South Africa in 1971 and he joined Tesla in 2004.
# """

prompt = prompt_template

# @app.route("/riddle")
# def riddle():
#     completion = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=32, temperature=0.7)
#     generated = completion.choices[0].text
#     print(generated)
#     if "Paragraph" in generated:
#         ind = generated.index("Paragraph") 
#     response = generated[:ind]
#     # response = generate_response()
#     return response

def generate_response():
    topic = "steakhouse dinner"
    gpt3_prompt = f'''The following is a conversation with an AI assistant riddler. The assistant is creative, clever, very friendly and always ask a question.
                    AI asking a question about chocolate: Great answer, how much water does 100g of chocolate require?
                    Human answering: About 1700 Liters of water
                    AI asking a question about person and water: What is the average water consumption of a person?
                    Human answering: 101 gallons per day.
                    AI asking a question about water and {topic}:
                    '''
    #Incorporate answer of previous question

    openai.api_key = "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"
    
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=gpt3_prompt,
        temperature=0,
        max_tokens=144,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n\n"],
        n=3,
    )
    return response


if __name__ == '__main__':

    app.run(debug=True)
