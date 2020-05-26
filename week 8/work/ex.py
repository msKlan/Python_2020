import pymysql
from sqlalchemy import create_engine
import pandas as pd
from flask import Flask
import json

con= pymysql.connect(host="localhost", port=3307, user="dev", password="ax2", db="statskode")
engine = create_engine('mysql+pymysql://dev:ax2@localhost:3307/statskode')
table_name = "statskode"

def import_data():
    data = pd.read_csv("befkbhalderstatkode.csv")
    print(data[:5])
    data.to_sql(table_name, con=engine, if_exists='replace', index=False)

def get_data():
    sql_query = f'SELECT * FROM {table_name}'
    data = None
    with con.cursor() as cursor:
        cursor.execute(sql_query)
        data = cursor.fetchall()
    print(data[:3])
    return data

app = Flask(__name__)
@app.route("/")
def index():
    return json.dumps(get_data())

@app.route("/load")
def load():
    import_data()
    return "Data loaded"


if __name__ == "__main__":
    app.run(debug=True)
