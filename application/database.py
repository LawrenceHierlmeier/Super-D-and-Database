from database_connection import DatabaseConnection


def list_characters():
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM CHARACTER")

        chars = [{'name': row[0], 'race': row[1], 'class': row[2]} for row in cursor.fetchall()]

        return chars


def get_race_attributes(race):
    with DatabaseConnection('CS2300Proj.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"SELECT * from RACE WHERE NAME = ?", (race,))

        race_attributes = [{'name': row[0], 'size': row[1], 'speed': row[2]} for row in cursor.fetchall()]

        return race_attributes

