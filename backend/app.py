from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )

@app.route("/points", methods=["GET"])
def get_points():
    category = request.args.get("category")
    conn = get_db_connection()
    cur = conn.cursor()

    if category:
        cur.execute(
            "SELECT id, name, description, category, ST_AsText(location) FROM points_of_interest WHERE category = %s",
            (category,)
        )
    else:
        cur.execute(
            "SELECT id, name, description, category, ST_AsText(location) FROM points_of_interest"
        )

    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "category": row[3],
            "location": row[4]
        })

    return jsonify(result)

@app.route("/points", methods=["POST"])
def add_point():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO points_of_interest (name, description, category, location)
        VALUES (%s, %s, %s, ST_MakePoint(%s, %s))
        """,
        (
            data["name"],
            data["description"],
            data["category"],
            data["longitude"],
            data["latitude"]
        )
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "Point added"}), 201

@app.route("/")
def home():
    return "API de Puntos de Interés funcionando ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
