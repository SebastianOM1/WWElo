import sqlite3

def search_promotion(promo_id):
    conn = sqlite3.connect('wrestling.db')
    cursor = conn.cursor()

    cursor.execute(
    '''
    SELECT * FROM promotions WHERE promotion_id = {}
    '''.format(promo_id))
    row = cursor.fetchall()

    conn.commit()
    conn.close()
    return row

def search_event(event_id):
    conn = sqlite3.connect('wrestling.db')
    cursor = conn.cursor()

    cursor.execute(
    '''
    SELECT * FROM events WHERE event_id = {}
    '''.format(event_id))
    row = cursor.fetchall()

    conn.commit()
    conn.close()
    return row

def search_wrestler(wrestler_id):
    conn = sqlite3.connect('wrestling.db')
    cursor = conn.cursor()

    cursor.execute(
    '''
    SELECT * FROM wrestlers WHERE wrestler_id = {}
    '''.format(wrestler_id))
    row = cursor.fetchall()

    conn.commit()
    conn.close()
    return row

def search_match(match_id):
    conn = sqlite3.connect('wrestling.db')
    cursor = conn.cursor()

    cursor.execute(
    '''
    SELECT * FROM wrestler_matches WHERE wrestler_match_id = {}
    '''.format(match_id))
    row = cursor.fetchall()

    conn.commit()
    conn.close()
    return row