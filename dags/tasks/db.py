from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
import psycopg2

load_dotenv()


def connect_db():
    conn = psycopg2.connect(
        database=os.getenv("database"),
        user=os.getenv("user"),
        host=os.getenv("host"),
        password=os.getenv("password"),
        port=os.getenv("port"),
    )
    return conn


def get_sql_conn():
    return create_engine(
        f'postgresql+psycopg2://{os.getenv("user")}:{os.getenv("password")}@{os.getenv("host")}:{os.getenv("port")}/{os.getenv("database")}'
    )


def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Athletes ( id integer PRIMARY KEY, name varchar, name_short varchar,gender varchar,country_code varchar,country varchar,height float,weight float,disciplines varchar,events varchar,birth_date date,coach varchar)"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Events (id integer PRIMARY KEY,event varchar,tag varchar,sport varchar,sport_code varchar)"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Medals (id integer PRIMARY KEY,medal_type varchar,medal_code varchar,medal_date date,athlete_id integer,event_id integer)"
    )
    cur.execute(
        "ALTER TABLE Medals ADD FOREIGN KEY (athlete_id) REFERENCES Athletes (code)"
    )
    cur.execute("ALTER TABLE Medals ADD FOREIGN KEY (event_id) REFERENCES Events (id)")
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    conn.close()
