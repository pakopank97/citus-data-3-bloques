from flask import Flask, jsonify
import psycopg2
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_CONFIG = {
    "host": os.getenv("DATABASE_HOST", "localhost"),
    "port": os.getenv("DATABASE_PORT", "5432"),
    "user": os.getenv("DATABASE_USER", "postgres"),
    "password": os.getenv("DATABASE_PASSWORD", "postgres"),
    "dbname": os.getenv("DATABASE_NAME", "demo")
}

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

@app.route("/usuarios")
def usuarios():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre TEXT
        );
    """)
    cur.execute("""
        INSERT INTO usuarios(nombre)
        VALUES ('Francisco'), ('Daniel'), ('Martínez')
        ON CONFLICT DO NOTHING;
    """)
    conn.commit()
    cur.execute("SELECT * FROM usuarios;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)