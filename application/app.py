from flask import Flask, render_template, request
from flask_navigation import Navigation

import database

app = Flask(__name__)
nav = Navigation(app)
#dungeon_database.create_class_table()

# Initializing Navigation
nav.Bar('top', [
    nav.Item('Home', 'home'),
    nav.Item('Characters', 'character_list'),
    nav.Item('Add Character', 'insert_character'),
    nav.Item('Add Campaign', 'insert_campaign')
])


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/characters')
def character_list():
    chars = database.list_characters()
    race_stats = []

    for character in chars:
        race_stats = database.get_race_attributes(chars[0]['race'])

    print(chars[0]['race'])
    print(race_stats)

    return render_template('character_list.html', chars=chars, race_stats=race_stats)

@app.route('/add_character', methods=["GET", "POST"])
def insert_character():
    if request.method == "POST":
        name = request.form['Name']
        intelligence = request.form['Intelligence']
        strength = request.form['Strength']
        dexterity =  request.form['Dexterity']
        wisdom = request.form['Wisdom']
        constitution = request.form['Constitution']
        charisma = request.form['Charisma']
    return render_template('add_character.html')

@app.route('/add_campaign', methods=["GET", "POST"])
def insert_campaign():
    if request.method == "POST":
        name = request.form['Name']
        region = request.form['Region']
        NPCS = request.form['NPCS']
    return render_template('add_campaign.html')

if __name__ == '__main__':
    app.run(debug=True)
