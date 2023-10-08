import psycopg2
from psycopg2 import sql
from settings import *

#Connecting to db
conn = psycopg2.connect(f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASS} port=5432")

def create_mm_dept():
    cur = conn.cursor()
    cur.execute(
            sql.SQL(    "CREATE TABLE mm.dept (" +
                        "id serial PRIMARY KEY," +
                        "name VARCHAR ( 50 ) NOT NULL," +
                        "create_dt date," +
                        "dates2 date)"
  )    
)
    conn.commit()

def insert_mm_dept():
    cur = conn.cursor()
    cur.execute(
        sql.SQL(
                "insert into mm.dept (id, name)" +
                "values" +
                "('1', 'Терапевтическое отделение')," +
                "('2', 'Хирургическое отделение')," +
                "('3', '2 кардиологическое (ОИМ)')," +
                "('4', 'Приемное отделение')," +
                "('5', 'Неврологическое отделение')"
        )
    )
    conn.commit()

def create_mm_tap():
    cur = conn.cursor()
    cur.execute(
        sql.SQL(
            
        )
    )