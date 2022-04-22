from database_connection import DatabaseConnection


def list_characters():
    with DatabaseConnection('dungeon_data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Character")

        chars = [{'name': row[0], 'race': row[1], 'class': row[2]} for row in cursor.fetchall()]

        return chars

def get_character_info(name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT C.NAME, C.RACE_NAME, S.NAME, H.CLASS_NAME, C.CAMPAIGN_NAME, P.FEAT_NAME" \
                         "       C.INTELLIGENCE, C.STRENGTH, C.DEXTERITY, C.WISDOM, C.CONSTITUTION, C. CHARISMA, " \
                         "FROM CHARACTER AS C, POSSESSES AS P, HAS AS H, SUB_RACE AS S" \
                         "WHERE (C.NAME = ? AND C.NAME = P.CHARACTER_NAME AND C.NAME = H.CHARACTER_NAME " \
                         "       AND C.RACE_NAME = S.PRIMARY_RACE_NAME)"
        cursor.execute(retrieve_query, name)

        tuples = cursor.fetchall()
        cursor.close()
        return tuples

def delete_character(name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()
        
        delete_query = "DELETE FROM CHARACTER " \
                       "WHERE NAME = ?"
        cursor.execute(delete_query, name)
        cursor.commit()
        cursor.close()
        return
  
def add_feat_to_character(character_name, feat_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        insert_query = "INSERT INTO POSSESSES VALUES(?, ?)"
        cursor.execute(insert_query, (character_name, feat_name))
        cursor.commit()
        cursor.close()
        return

def add_class_to_character(character_name, class_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        insert_query = "INSERT INTO HAS VALUES(?, ?)"
        cursor.execute(insert_query, (class_name, character_name))
        cursor.commit()
        cursor.close()
        return

def modify_character(old_name, new_name, intelligence, strength, dexterity, wisdom, constitution, charisma, race_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        update_query = "UPDATE CHARACTER " \
                       "SET NAME = ?, INTELLIGENCE = ?, STRENGTH = ?, DEXTERITY = ?, WISDOM = ?, CONSTITUTION = ?," \
                       "    CHARISMA = ?, RACE_NAME = ?" \
                       "WHERE NAME = ?"
        cursor.execute(update_query, (new_name, intelligence, strength, dexterity,
                                      wisdom, constitution, charisma, race_name, old_name))
        cursor.commit()
        cursor.close()
        return

def delete_campaign(campaign_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()
    
        delete_query = "DELETE FROM CAMPAIGN " \
                       "WHERE NAME = ?"
        cursor.execute(delete_query, campaign_name)
        cursor.commit()
        cursor.close()
        return

def remove_character_from_campaign(character_name, campaign_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()
        #set campaign_name in CHARACTER to 'None'
        update_query1 = "UPDATE CHARACTER" \
                       "SET CAMPAIGN_NAME = 'None'" \
                       "WHERE NAME = ? AND CAMPAIGN_NAME = ?"
        cursor.execute(update_query1, (character_name, campaign_name))
        #decrement campaign player count
        update_query2 = "UPDATE CAMPAIGN" \
                       "SET NUM_PLAYERS = NUM_PLAYERS-1" \
                       "WHERE NAME = ?"
        cursor.execute(update_query2, (campaign_name))
        cursor.commit()
        cursor.close()
        return

def add_item_to_inventory(item, item_weight, character_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        add_query = "INSERT INTO INVENTORY VALUES (?, ?, ?)"
        cursor.execute(add_query, (item, item_weight, character_name))
        cursor.commit()
        cursor.close()
        return

def get_character_inventory(character_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT * " \
                         "FROM INVENTORY AS I " \
                         "WHERE I.CHARACTER_NAME = ?"
        cursor.execute(retrieve_query, character_name)
        inventory = cursor.fetchall()
        cursor.commit()
        cursor.close()
        return inventory

def add_character_to_campaign(campaign_name, character_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        update_query = "UPDATE CHARACTER " \
                       "SET CAMPAIGN_NAME = ? " \
                       "WHERE NAME = ?"
        cursor.execute(update_query, (campaign_name, character_name))
        cursor.commit()
        cursor.close()
        return

def add_campaign(name, region, num_npcs):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        insert_query = "INSERT INTO CAMPAIGN(NAME, REGION, NPCS) VALUES (?, ?, ?)"
        cursor.execute(insert_query, (name, region, num_npcs))
        cursor.commit()
        cursor.close()
        return

def add_character(name, intelligence, strength, dexterity, wisdom, constitution, charisma, race_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()
        #insert into CHARACTER table
        insert_query = "INSERT INTO CHARACTER VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(insert_query,
                       (name, intelligence, strength, dexterity, wisdom, constitution, charisma, race_name))
        cursor.commit()
        cursor.close()
        return
