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
    nav.Item('Character Page', 'character_page', {'character_name': 'none'}),
    nav.Item('Campaigns', 'campaign_list'),
    nav.Item('Races', 'race_list'),
    nav.Item('Classes', 'class_list'),
    nav.Item('Feats', 'feat_list'),
    nav.Item('Add Character', 'insert_character'),
    #nav.Item('Modify Character', ''),
    nav.Item('Add Campaign', 'insert_campaign'),
    nav.Item('Add Character to Campaign', 'add_char_to_campaign'),
    nav.Item('Edit Campaign', 'edit_campaign'),
    nav.Item('Add Feat to Character', 'character_feat'),
    nav.Item('Class and Race Combinations', 'class_race_combos')
    #nav.Item('Remove Feat from Character', '')
])


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/characters')
def character_list():
    chars = database.list_characters()
    # print(chars)
    # print(len(chars))

    character_tuple = []

    for i in range(len(chars)):
        character_tuple.append(database.get_character_info(chars[i]['name']))

    # print(character_tuple)

    return render_template('character_list.html', chars=character_tuple)


@app.route('/characters/<character_name>')
def character_page(character_name):
    character = database.get_character_info(character_name)
    print(character)
    race_info = database.get_race_info(character[0]['race'])
    print(race_info)
    class_info = database.get_class_info(character[0]['class'])
    print(class_info)
    return render_template('character_page.html', character=character, race_info=race_info, class_info=class_info)


@app.route('/add_character', methods=["GET", "POST"])
def insert_character():
    #get names of fastest and slowest race
    #fastest_race = database.max_race_speed()
    #slowest_race = database.min_race_speed()
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
        database.add_campaign(name, region, NPCS)
    return render_template('add_campaign.html')


@app.route('/edit_campaign', methods=['GET', 'POST'])
def edit_campaign():
    campaigns = database.list_campaigns() #get list of campaign names
    if request.method == "POST":
        if request.form['submit'] == 'Delete Campaign':
            campaign_to_delete = request.form['old_name']
            print("campaign deleted")
            database.delete_campaign(campaign_to_delete)
        elif request.form['submit'] == 'Update':
            old_name = request.form['old_name']
            new_name = request.form['new_name']
            region = request.form['region']
            num_npcs = request.form['num_npcs']
            database.modify_campaign(old_name, new_name, region, num_npcs)
            print("campaign updated")
            print(old_name, new_name, region, num_npcs)
    return render_template('edit_campaign.html', campaigns=campaigns)


@app.route('/add_feat_to_character', methods=["GET", "POST"])
def character_feat():
    feat_names = database.list_feats()
    character_names = database.list_characters()
    if (len(character_names) == 0):
        print("Add a Character First!")
        return render_template('home.html')

    if request.method == "POST":
        chosen_name = request.form['chosen_name']
        chosen_feat = request.form['chosen_feat']
        print(chosen_name, chosen_feat)
        database.add_feat_to_character(chosen_name, chosen_feat)

    return render_template('add_feat_to_character.html', characters=character_names, feats=feat_names)

@app.route('/add_to_inventory', methods =["GET", "POST"])
def insert_character_inventory():
    if request.method == "POST":
        character_name = request.form['Character_Name']
        item_name = request.form['Item_Name']
        item_weight = request.form['Item_Weight']
        database.add_item_to_inventory(item_name, item_weight, character_name)
    return render_template('add_to_inventory.html')


@app.route('/add_char_to_campaign', methods=["GET", "POST"])
def add_char_to_campaign():
    campaigns = database.list_campaigns()
    characters = database.list_characters()
    if (len(characters) == 0):
        print("Add a Character First!")
        return render_template("home.html")

    if request.method == "POST":
        character_name = request.form['chosen_name']
        campaign_name = request.form['chosen_campaign']
        database.add_character_to_campaign(campaign_name, character_name)
        print(character_name, campaign_name)
    return render_template('add_char_to_campaign.html', characters=characters, campaigns=campaigns)


@app.route('/class_list', methods=["GET", "POST"])
def class_list():
    classes = database.list_classes()
    print(classes)
    print(len(classes))

    class_tuple = []

    for i in range(len(classes)):
        class_tuple.append(database.get_class_info(classes[i]['name']))


    print(class_tuple)
    return render_template("class_list.html", classes=class_tuple)


@app.route('/race_list', methods=["GET", "POST"])
def race_list():
    races = database.list_races()
    print(races)
    print(len(races))

    race_tuple = []

    for i in range(len(races)):
        race_tuple.append(database.get_race_info(races[i]['name']))

    print(race_tuple)
    return render_template("race_list.html", races=race_tuple)

@app.route('/race_list/subrace', methods=["GET", "POST"])
def subrace_list():
    selected_primary_race = request.args.get('type')

    subraces = database.list_subraces(selected_primary_race)
    print(subraces)
    print(len(subraces))

    subrace_tuple = []

    for i in range(len(subraces)):
        subrace_tuple.append(database.get_subrace_info(subraces[i]['name']))
    print(subrace_tuple)

    print("on sub races page", selected_primary_race)

    return render_template("subrace_list.html", subraces=subrace_tuple, primary_race=selected_primary_race)


@app.route('/feat_list', methods=["GET", "POST"])
def feat_list():
    feats = database.list_feats()
    print(feats)
    print(len(feats))

    feat_tuple = []

    for i in range(len(feats)):
        feat_tuple.append(database.get_feat_info(feats[i]['name']))

    print(feat_tuple)
    return render_template("feat_list.html", feats=feat_tuple)


@app.route('/campaign_list', methods=["GET", "POST"])
def campaign_list():
    campaigns = database.list_campaigns()
    print(campaigns)
    print(len(campaigns))

    campaign_tuple = []

    for i in range(len(campaigns)):
        if (campaigns[i]['name'] != "None"):
            campaign_tuple.append(database.get_campaign_info(campaigns[i]['name']))

    print(campaign_tuple)
    return render_template("campaign_list.html", campaigns=campaign_tuple)

@app.route('/class_race_combos', methods=["GET", "POST"])
def class_race_combos():
    combos = database.class_race_combination()
    print(combos)
    return render_template("class_race_combos.html", combos=combos)


if __name__ == '__main__':
    app.run(debug=True)
