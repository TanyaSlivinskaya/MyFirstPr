import sqlite3
from datetime import datetime

def insert_events(cursor, events_data):
    cursor.executemany("INSERT INTO events (name, date, venue_id) VALUES (?, ?, ?)", events_data)

def insert_tickets(cursor, event_id, tickets_data):
    for ticket_data in tickets_data:
        cursor.execute("INSERT INTO tickets (event_id, price) VALUES (?, ?)", (event_id, ticket_data))

def insert_venues(cursor, venues_data):
    for venue_data in venues_data:
        cursor.execute("INSERT INTO venues (name, address, capacity) VALUES (?, ?, ?)", venue_data)

connection = sqlite3.connect('tickets.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        date DATE NOT NULL,
        venue_id INTEGER, 
        FOREIGN KEY (venue_id) REFERENCES venues(id) 
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        capacity INTEGER
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        event_id INTEGER,
        price REAL,
        FOREIGN KEY (event_id) REFERENCES events(id)
    )
""")

events_data = [
    ("circus", datetime.strptime('2024-05-27', '%Y-%m-%d'), 1),
    ("concert", datetime.strptime('2023-05-27', '%Y-%m-%d'), 2),
    ("theater", datetime.strptime('2022-05-27', '%Y-%m-%d'), 3)
]

insert_events(cursor, events_data)

cursor.execute("SELECT * FROM events WHERE name=?", ("circus",))
event = cursor.fetchone()
print("Circus event:", event)

new_date = '2024-05-26'
cursor.execute("UPDATE events SET date=? WHERE name=?", (new_date, "theater"))

event_id = 1
tickets_data = [100.0, 150.0, 200.0]
insert_tickets(cursor, event_id, tickets_data)

venues_data = [
    ('Theater', 'sovetskaya', 1300),
    ('Concert Hall', 'Lenina', 1500),
    ('Stadium', 'oktyabria', 10000)
]
insert_venues(cursor, venues_data)

connection.commit()
connection.close()