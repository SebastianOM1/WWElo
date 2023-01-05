import sqlite3

def create():
    conn = sqlite3.connect('wrestling.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS promotions (
        promotion_id INTEGER,
        name TEXT,
        founded DATE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        event_id INTEGER,
        name TEXT,
        location TEXT,
        date DATE,
        promotion_id INTEGER,
        FOREIGN KEY (promotion_id) REFERENCES promotions(promotion_id)
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS wrestlers (
        wrestler_id INTEGER,
        name TEXT,
        birthday DATE,
        promotion_id INTEGER,
        FOREIGN KEY (promotion_id) REFERENCES promotions(promotion_id)
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS wrestler_matches (
        wrestler_match_id INTEGER,
        wrestler_id INTEGER,
        match_id INTEGER,
        result TEXT,
        FOREIGN KEY (wrestler_id) REFERENCES wrestlers(wrestler_id),
        FOREIGN KEY (match_id) REFERENCES matches(match_id)
    );
    ''')
    conn.commit()
    conn.close()

create()