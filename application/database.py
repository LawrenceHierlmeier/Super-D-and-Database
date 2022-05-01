from database_connection import DatabaseConnection


def list_characters():
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM CHARACTER")

        chars = [{'name': row[0]} for row in cursor.fetchall()]

        return chars


# testing code, may keep
def get_race_attributes(race):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"SELECT * from RACE WHERE NAME = ?", (race,))

        race_attributes = [{'name': row[0], 'size': row[1], 'speed': row[2]} for row in cursor.fetchall()]

        return race_attributes


def get_character_info(name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT C.NAME, C.RACE_NAME, H.CLASS_NAME, " \
                         "C.STRENGTH, C.DEXTERITY, C.CONSTITUTION, C.INTELLIGENCE, C.WISDOM, C.CHARISMA " \
                         "FROM CHARACTER AS C, HAS AS H " \
                         "WHERE (C.NAME = ? AND C.NAME = H.CHARACTER_NAME)"

        # retrieve_query = "SELECT C.NAME, C.RACE_NAME, H.CLASS_NAME, C.CAMPAIGN_NAME, P.FEAT_NAME," \
        #                 "       C.INTELLIGENCE, C.STRENGTH, C.DEXTERITY, C.WISDOM, C.CONSTITUTION, C.CHARISMA " \
        #                 "FROM CHARACTER AS C, POSSESSES AS P, HAS AS H " \
        #                "WHERE (C.NAME = ? AND C.NAME = P.CHARACTER_NAME AND C.NAME = H.CHARACTER_NAME)"
        # "       AND C.RACE_NAME = S.PRIMARY_RACE_NAME)"

        cursor.execute(retrieve_query, (name,))

        char_attributes = [{'name': row[0], 'race': row[1], 'class': row[2],
                            'strength': row[3], 'dexterity': row[4], 'constitution': row[5],
                            'intelligence': row[6], 'wisdom': row[7], 'charisma': row[8]} for row in cursor.fetchall()]

        return char_attributes


def delete_character(name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        delete_query = "DELETE FROM CHARACTER " \
                       "WHERE NAME = ?"
        cursor.execute(delete_query, (name,))

        return


def list_races():
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT NAME " \
                         "FROM RACE"
        cursor.execute(retrieve_query)

        races = [{'name': row[0]} for row in cursor.fetchall()]

        return races

def get_race_info(race_name):  # use to display all races information
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT * " \
                         "FROM RACE " \
                         "WHERE NAME = ?"

        cursor.execute(retrieve_query, (race_name,))
        race_attributes = [{'name': row[0], 'feats': row[1], 'languages': row[2], 'proficiencies': row[3],
                            'AS_name': row[4], 'AS_inc_val': row[5], 'speed': row[6],
                            'size': row[7]} for row in cursor.fetchall()]


        return race_attributes


def list_subraces(primary_race):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT NAME " \
                         "FROM SUB_RACE " \
                         "WHERE PRIMARY_RACE_NAME = ?"
        cursor.execute(retrieve_query, (primary_race,))

        subraces = [{'name': row[0]} for row in cursor.fetchall()]

        return subraces

def get_subrace_info(subrace_name):  # use to display subrace info of primary race
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT * " \
                         "FROM SUB_RACE " \
                         "WHERE NAME = ?"
        cursor.execute(retrieve_query, (subrace_name,))
        subrace_attributes = [{'name': row[0], 'proficiencies': row[1], 'AS_name': row[2], 'AS_inc_val': row[3],
                               'feats': row[4], 'primary_race_name': row[5]} for row in cursor.fetchall()]

        return subrace_attributes

def list_classes():
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT NAME " \
                         "FROM CLASS"
        cursor.execute(retrieve_query)

        classes = [{'name': row[0]} for row in cursor.fetchall()]

        return classes


def get_class_info(class_name):  # use to display all classes information
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT * " \
                         "FROM CLASS " \
                         "WHERE NAME = ?"

        cursor.execute(retrieve_query, (class_name,))
        class_attributes = [{'name': row[0], 'hit_die': row[1], 'saving_throws': row[2], 'proficiencies': row[3],
                             'prof_bonus': row[4], 'feats': row[5], 'AS_name': row[6],
                             'AS_inc_val': row[7]} for row in cursor.fetchall()]

        return class_attributes


def list_feats():
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT NAME " \
                         "FROM FEATS"
        cursor.execute(retrieve_query)

        feats = [{'name': row[0]} for row in cursor.fetchall()]

        return feats

def get_feat_info(feat_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT * " \
                         "FROM FEATS " \
                         "WHERE NAME = ?"
        cursor.execute(retrieve_query, (feat_name,))
        feat_attributes = [{'name': row[0], 'prerequisites': row[1], 'description': row[2]} for row in cursor.fetchall()]

        return feat_attributes


def add_feat_to_character(character_name, feat_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        insert_query = "INSERT INTO POSSESSES VALUES(?, ?)"
        cursor.execute(insert_query, (character_name, feat_name,))

        return


def add_class_to_character(character_name, class_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        insert_query = "INSERT INTO HAS VALUES(?, ?)"
        cursor.execute(insert_query, (class_name, character_name,))
        return


def modify_character(old_name, new_name, intelligence, strength, dexterity, wisdom, constitution, charisma, race_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        update_query = "UPDATE CHARACTER " \
                       "SET NAME = ?, INTELLIGENCE = ?, STRENGTH = ?, DEXTERITY = ?, WISDOM = ?, CONSTITUTION = ?," \
                       "    CHARISMA = ?, RACE_NAME = ? " \
                       "WHERE NAME = ?"
        cursor.execute(update_query, (new_name, intelligence, strength, dexterity,
                                      wisdom, constitution, charisma, race_name, old_name,))

        return


def delete_campaign(campaign_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        delete_query = "DELETE FROM CAMPAIGN " \
                       "WHERE NAME = ?"
        cursor.execute(delete_query, (campaign_name,))

        return


def remove_character_from_campaign(character_name, campaign_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()
        # set campaign_name in CHARACTER to 'None'
        update_query1 = "UPDATE CHARACTER " \
                        "SET CAMPAIGN_NAME = 'None' " \
                        "WHERE NAME = ? AND CAMPAIGN_NAME = ?"
        cursor.execute(update_query1, (character_name, campaign_name,))
        # decrement campaign player count
        update_query2 = "UPDATE CAMPAIGN " \
                        "SET NUM_PLAYERS = NUM_PLAYERS-1 " \
                        "WHERE NAME = ?"
        cursor.execute(update_query2, (campaign_name,))

        return


def num_items_in_inventory(character_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT COUNT(ITEM) " \
                         "FROM INVENTORY " \
                         "WHERE CHARACTER_NAME = ?"
        cursor.execute(retrieve_query, (character_name,))
        num = cursor.fetchone()

        return num[0]


def inventory_weight(character_name):  # retrieves the weight of a character's inventory
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT SUM(ITEM_WEIGHT) " \
                         "FROM INVENTORY AS I " \
                         "WHERE CHARACTER_NAME = ?"
        cursor.execute(retrieve_query, (character_name,))
        weight = cursor.fetchone()

        return weight[0]


def add_item_to_inventory(item, item_weight, character_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()
        # get character strength score to calculate inventory weight capacity
        retrieve_query = "SELECT STRENGTH " \
                         "FROM CHARACTER " \
                         "WHERE NAME = ?"
        cursor.execute(retrieve_query, (character_name,))
        capacity = cursor.fetchone()
        # if adding item keeps weight below or at capacity
        if (inventory_weight(character_name) + item_weight <= capacity[0]):
            add_query = "INSERT INTO INVENTORY VALUES (?, ?, ?)"
            cursor.execute(add_query, (item, item_weight, character_name,))
        else:  # over capacity
            print("Item is too heavy.")

        return


def get_character_inventory(character_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT ITEM, ITEM_WEIGHT " \
                         "FROM INVENTORY " \
                         "WHERE CHARACTER_NAME = ?"
        cursor.execute(retrieve_query, (character_name,))
<<<<<<< HEAD
        inventory = cursor.fetchall()
=======
        inventory = [{'item': row[0], 'item_weight': row[1]} for row in cursor.fetchall()]
>>>>>>> 74de12a10068281abbe40a567fa8cd7e97da3b78

        return inventory


def add_character_to_campaign(campaign_name, character_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        update_query1 = "UPDATE CHARACTER " \
                       "SET CAMPAIGN_NAME = ? " \
<<<<<<< HEAD
                       "WHERE (NAME = ?)"
        cursor.execute(update_query, (campaign_name, character_name,))
=======
                       "WHERE NAME = ?"
        cursor.execute(update_query1, (campaign_name, character_name,))
        #increment number of players count in specific campaign tuple
        update_query2 = "UPDATE CAMPAIGN " \
                        "SET NUM_PLAYERS = NUM_PLAYERS+1 " \
                        "WHERE NAME = ?"
        cursor.execute(update_query2, (campaign_name,))
>>>>>>> 74de12a10068281abbe40a567fa8cd7e97da3b78

        return


def add_campaign(name, region, num_npcs):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        insert_query = "INSERT INTO CAMPAIGN(NAME, REGION, NPCS) VALUES (?, ?, ?)"
        cursor.execute(insert_query, (name, region, num_npcs,))

        return


def list_campaigns():
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT NAME " \
                         "FROM CAMPAIGN"
        cursor.execute(retrieve_query)

        campaigns = [{'name': row[0]} for row in cursor.fetchall()]

        return campaigns


def get_campaign_info(campaign_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        retrieve_query = "SELECT * " \
                         "FROM CAMPAIGN " \
                         "WHERE NAME = ?"
        cursor.execute(retrieve_query, (campaign_name,))
        campaign_attributes = [{'name': row[0], 'region': row[1], 'num_players': row[2],
                                'NPCS': row[3]} for row in cursor.fetchall()]

        return campaign_attributes


def modify_campaign(old_name, new_name, region, num_npcs):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        update_query = "UPDATE CAMPAIGN " \
                       "SET NAME = ?, REGION = ?, NPCS = ? " \
                       "WHERE NAME = ?"
        cursor.execute(update_query, (new_name, region, num_npcs, old_name,))


def add_character(name, intelligence, strength, dexterity, wisdom, constitution, charisma, race_name, campaign_name):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()
        # insert into CHARACTER table
        insert_query = "INSERT INTO CHARACTER VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(insert_query,
                       (name, intelligence, strength, dexterity, wisdom, constitution, charisma, race_name,
                        campaign_name,))
        return


def min_race_speed():
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()
        # gets names of slowest races and respective speeds
        retrieve_query = "SELECT R1.NAME, R1.SPEED " \
                         "FROM RACE AS R1 " \
                         "WHERE R1.SPEED = (SELECT MIN(SPEED) " \
                         "                  FROM RACE AS R2)"
        cursor.execute(retrieve_query)
        races = [{'name': row[0], 'speed': row[1]} for row in cursor.fetchall()]

        return races


def max_race_speed():
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()
        # gets names of fastest races and respective speeds
        retrieve_query = "SELECT R1.NAME, R1.SPEED " \
                         "FROM RACE AS R1 " \
                         "WHERE R1.SPEED = (SELECT MAX(SPEED) " \
                         "                  FROM RACE AS R2)"
        cursor.execute(retrieve_query)
        races = [{'name': row[0], 'speed': row[1]} for row in cursor.fetchall()]

        return races
