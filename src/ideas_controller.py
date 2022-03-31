from create_tables import get_db

def insert_idea(value, maturityLevel, FullText):
    try:
        print("In the insert")
        db = get_db()
        cursor = db.cursor()
        # INSERT INTO ideas (value, maturityLevel, tags, FullText) values("Hello","3","there","yuhuu");
        statement = "INSERT INTO ideas (value, maturityLevel, FullText) values (?, ?, ?)"
        print(statement + "  :" + value + " " + maturityLevel + " " + FullText)
        cursor.execute(statement, [value, maturityLevel, FullText])
        db.commit()
    except Exception as er:
        print('Insert error: '+er)
    return True

def get_by_id(id):
    try:
        db = get_db()
        cursor = db.cursor()
        statement = "SELECT * FROM ideas WHERE id = ?"
        cursor.execute(statement, [id])
    except Exception as er:
        print('Get by id error: '+er)
    return cursor.fetchone()


def get_ideas():
    try:
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM ideas"
        cursor.execute(query)
    except Exception as er:
        print('Get all error: '+er)
    return cursor.fetchall()

def update_idea(id, value, maturityLevel, FullText):
    try:
        db = get_db()
        cursor = db.cursor()
        statement = "UPDATE ideas SET value = ?, maturityLevel = ?, FullText = ? WHERE id = ?"
        cursor.execute(statement, [value, maturityLevel, FullText, id])
        db.commit()
    except Exception as er:
        print('Update Idea error: '+er)
    return True


def delete_idea(id):
    try:
        db = get_db()
        cursor = db.cursor()
        statement = "DELETE FROM ideas WHERE id = ?"
        cursor.execute(statement, [id])
        db.commit()
    except Exception as er:
        print('Delete Idea error: '+ er)
    return True
