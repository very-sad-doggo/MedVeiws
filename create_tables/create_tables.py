import psycopg2
from psycopg2 import sql
from settings import *

#Connecting to db
conn = psycopg2.connect(f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASS} port=5432")

def create_mm_dept():
    cur = conn.cursor()
    cur.execute(
            sql.SQL("")    
    )