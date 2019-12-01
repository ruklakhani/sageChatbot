from flask import Flask, render_template, request
from random import randint 
import requests

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/chatbot', methods=['GET','POST'])
def welcome(): 
    return render_template('chatbot_form.html')

@app.route('/chatbot_results')
def chatbot_results():
    q1 = request.args.get('q1')
    q2 = request.args.get('q2')
    q3 = request.args.get('q3')

# question_prompts = [
#     "How are you feeling today?\n(a) amazing \n(b) good \n(c) alright \n(d) eh \n(e) not great \n(f) really bad\n\n"
#     "What is making you feel that way?\n(a) work \n(b) school \n(c) friends \n(d) family \n(e) health \n(f) other\n\n"
# ]
# questions = [
#     Question(question_prompts[0],)
# ]