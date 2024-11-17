import sys
import psycopg2

# def connect_db():
conn = psycopg2.connect(
    database="olympic2024",
    user="postgres",
    host="localhost",
    password="mysecretpassword",
    port=5431,
)


def create_db():

    cur = conn.cursor()
    cur.execute("""CREATE DATABASE olympic2024""")
    # Make the changes to the database persistent
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    conn.close()


def create_tables():
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE Athletes ( id integer PRIMARY KEY, name varchar, name_short varchar,gender varchar,country_code varchar,country varchar,height float,weight float,disciplines varchar,events varchar,birth_date datetime,coach varchar)"
    )
    cur.execute(
        "CREATE TABLE Events (id integer PRIMARY KEY,event varchar,tag varchar,sport varchar,sport_code varchar)"
    )
    cur.execute(
        "CREATE TABLE Medals (id integer PRIMARY KEY,medal_type varchar,medal_code varchar,medal_date date,athlete_id integer,event_id integer)"
    )
    cur.execute(
        "ALTER TABLE Medals ADD FOREIGN KEY (athlete_id) REFERENCES Athletes (id)"
    )
    cur.execute("ALTER TABLE Medals ADD FOREIGN KEY (event_id) REFERENCES Events (id)")
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    conn.close()
