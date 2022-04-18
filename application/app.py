from flask import Flask
import database

app = Flask(__name__)
#dungeon_database.create_class_table()


@app.route('/')
def home():
    return 'Hello World'


@app.route('/characters')
def character_list():
    chars = dungeon_database.list_characters()
    char_list = ' '.join(str(e) for e in chars)

    return char_list


if __name__ == '__main__':
    app.run(debug=True)