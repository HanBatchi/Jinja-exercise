from flask import Flask, render_template, request, redirect, url_for
from stories import Story, initial_story  


app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home_page():
#     if request.method == 'POST':
#           user_input = {
#                'place': request.form['place'],
#                'noun': request.form['noun'],
#                'verb': request.form['verb'],
#                'adjective': request.form['adjective'],
#                'plural_noun' : request.form['plural_noun'],
#           }
#           generated_story = story.generate(user_input)
#           return render_template('result.html', story = generated_story)
#     return render_template('form.html')

# @app.route('/story')
# def result_page():
#     return render_template('result.html')

@app.route('/')
def home():
    return render_template('form.html', prompts=initial_story.prompts)

@app.route('/story', methods=['POST'])
def show_story():
    answers = {}
    for prompt in initial_story.prompts:
        answers[prompt] = request.form[prompt]

    generated_story = initial_story.generate(answers)

    return render_template('result.html', story=generated_story)
