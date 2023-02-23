import string
from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

connection = psycopg2.connect(host = '34.132.44.118',
                              database = 'lab1-2',
                              user = 'postgres',
                              password = 'password')

@app.route('/asgeojson', methods=['GET', 'POST'])

def get_geojson():
    cursor = connection.cursor()
    cursor.execute("SELECT ST_AsGeoJSON(harriet_poly.*) AS poly_geojson FROM harriet_poly;")
   # result = cursor.fetchone()
    result = cursor.fetchall()
    return result[0][0]
    
    if result is None:
        return jsonify({'error': 'Polygon not found'}), 404
    else:
        return jsonify({'geojson': result[0]})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
