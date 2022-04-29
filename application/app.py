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
    #nav.Item('Modify Character', ''),
    #nav.Item('Remove Character', ''),
    nav.Item('Add Campaign', 'insert_campaign'),
    #nav.Item('Remove Campaign', ''),
    nav.Item('Add Feat to Character', 'character_feat')#,
    #nav.Item('Remove Feat from Character', '')
])


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/characters')
def character_list():
    chars = database.list_characters()
    print(chars)
    print(len(chars))

    character_tuple = []

    for i in range(len(chars)):
        character_tuple.append(database.get_character_info(chars[i]['name']))
    #race_stats = []

    #for character in chars:
    #    race_stats = database.get_race_attributes(chars[0]['race'])

    print(character_tuple)
    #print(race_stats)

    database.delete_character(chars[0]['name'])
    return render_template('character_list.html', chars=character_tuple)


@app.route('/add_character', methods=["GET", "POST"])
def insert_character():
    if request.method == "POST":
        name = request.form['Name']
        intelligence = request.form['Intelligence']
        strength = request.form['Strength']
        dexterity = request.form['Dexterity']
        wisdom = request.form['Wisdom']
        constitution = request.form['Constitution']
        charisma = request.form['Charisma']
        race = request.form['Race']
        character_class = request.form['Class']
        campaign_name = 'None'
        print(name, intelligence, strength, dexterity, wisdom, constitution, charisma, race, character_class)
        database.add_character(name, intelligence, strength, dexterity, wisdom, constitution, charisma, race, campaign_name)
        print(name, character_class)
        database.add_class_to_character(name, character_class)
    return render_template('add_character.html')


@app.route('/add_campaign', methods=["GET", "POST"])
def insert_campaign():
    if request.method == "POST":
        name = request.form['Name']
        region = request.form['Region']
        NPCS = request.form['NPCS']
    return render_template('add_campaign.html')


@app.route('/add_feat_to_character', methods=["GET", "POST"])
def character_feat():
    feat_attributes = {'Prereq': "",
                       'Description': ""}
    characters = ["Bob", "John", "Drax"]
    feats = ["Strong", "Agile", "Quick"]

    if request.method == "POST":
        chosen_name = request.form['chosen_name']
        chosen_feat = request.form['chosen_feat']
        feat_attributes = {'Prereq': "Level 12",
                           'Description': "Agile"}
    return render_template('add_feat_to_character.html', characters=characters, feats=feats,
                           feat_prereq=feat_attributes['Prereq'], feat_description=feat_attributes['Description'])


if __name__ == '__main__':
    app.run(debug=True)
