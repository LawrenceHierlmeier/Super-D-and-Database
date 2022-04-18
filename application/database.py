from database_connection import DatabaseConnection


def list_characters():
    with DatabaseConnection('dungeon_data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Character")

        chars = [{'name': row[0], 'race': row[1], 'class': row[2]} for row in cursor.fetchall()]

        return chars
