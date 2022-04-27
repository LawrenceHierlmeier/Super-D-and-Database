from flask import Flask, render_template
from flask_navigation import Navigation

import database

app = Flask(__name__)
nav = Navigation(app)
#dungeon_database.create_class_table()

# Initializing Navigation
nav.Bar('top', [
    nav.Item('Home', 'home'),
    nav.Item('Characters', 'character_list')
])


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/characters')
def character_list():
    chars = database.list_characters()
    print(chars[0]['name'])
    character_tuple = database.get_character_info(chars[0]['name'])
    #race_stats = []

    #for character in chars:
    #    race_stats = database.get_race_attributes(chars[0]['race'])

    print(character_tuple)
    #print(race_stats)

    return render_template('character_list.html', chars=chars)


if __name__ == '__main__':
    app.run(debug=True)
