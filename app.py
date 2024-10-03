from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "I love NYC"
debug = DebugToolbarExtension(app)

@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/story')
def get_story():
    verb = request.args['verb']
    noun = request.args['noun']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']
    place = request.args['place']


    story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time long-ago in {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )


    answer = {'place': place, 'adjective': adjective, 'noun': noun, 'verb': verb, 'plural_noun': plural_noun}

    story_text = story.generate(answer)

    return render_template('story.html', story = story_text)