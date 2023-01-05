import sqlite3
from search_table import search_promotion

def insert_promotion(promo_obj):
    conn = sqlite3.connect('wrestling.db')
    cursor = conn.cursor()

    cursor.execute(
    '''
    INSERT INTO promotions (promotion_id, name, founded) VALUES (?, ?, ?)
    ''',
    (promo_obj._id, promo_obj.name, None))

    conn.commit()
    conn.close()

def insert_event(event_obj):
    conn = sqlite3.connect('wrestling.db')
    cursor = conn.cursor()
    
    if not search_promotion(event_obj.promo._id):
        insert_promotion(event_obj.promo)

    cursor.execute(
    '''
    INSERT INTO events (event_id, name, location, date, promotion_id) VALUES (?, ?, ?, ?, ?)
    ''',
    (event_obj._id, event_obj.name, event_obj.location, event_obj.date, event_obj.promo._id))

    conn.commit()
    conn.close()

def insert_wrestler(wrestler_obj):
    conn = sqlite3.connect('wrestling.db')
    cursor = conn.cursor()

    conn.commit()
    conn.close()

def insert_match(match_obj):
    conn = sqlite3.connect('wrestling.db')
    cursor = conn.cursor()

    conn.commit()
    conn.close()