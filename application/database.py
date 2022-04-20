from database_connection import DatabaseConnection


def list_characters():
    with DatabaseConnection('dungeon_data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Character")

        chars = [{'name': row[0], 'race': row[1], 'class': row[2]} for row in cursor.fetchall()]

        return chars

def delete_character(name):
    with DatabaseConnection('dungeon_data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Character AS C WHERE C.name = name")

def add_feats():
    pass

def modify_character():
    pass

def delete_campaign():
    pass

def remove_character_from_campaign():
    pass

def add_item_to_inventory():
    pass

def show_character_inventory():
    pass

def add_character_to_campaign():
    pass

def add_campaign():
    pass

def add_character():
    pass
