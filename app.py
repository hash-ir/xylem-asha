from flask import Flask, render_template, request, redirect, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from multiprocessing import Value
import openai
import pandas as pd
import csv
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
openai.api_key = "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"
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
    1: "What is your company's name?",
    2: "Where are you based?",
    3: "How many employees do you have?",
    4: "What is your current iPERL Water Meter's reading?",
}

answers = []
i = 1

# @app.route('/', methods=['GET'])
# def welcome():
#     return render_template('home.html')

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
        # print(answer)
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

prompt_template= """

Paragraph: There is the same amount of water on Earth as there was when the Earth was formed. The water from your faucet could contain molecules that dinosaurs drank.
Question: How much water is there on Earth? Answer: The same amount as when the Earth was formed

Paragraph: Water regulates the Earth’s temperature. It also regulates the temperature of the human body, carries nutrients and oxygen to cells, cushions joints, protects organs and tissues, and removes wastes.
Question: What does water do? Answer: It regulates the Earth’s temperature

Paragraph: Nearly 97% of the world’s water is salty or otherwise undrinkable. Another 2% is locked in ice caps and glaciers. That leaves just 1% for all of humanity’s needs — all its agricultural, residential, manufacturing, community, and personal needs. Hence, water consumption is very necessary.
Question: Why is water consumption necessary? Answer: Only 1% of the world’s water is available for all of humanity’s needs — its agricultural, residential, manufacturing, community, and personal needs

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

@app.route("/riddle")
def riddle():
    completion = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=32, temperature=0.7)
    generated = completion.choices[0].text
    print(generated)
    if "Paragraph" in generated:
        ind = generated.index("Paragraph") 
    response = generated[:ind]
    # response = generate_response()
    return response

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
