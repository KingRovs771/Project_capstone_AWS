from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data (simulasi database)
data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Endpoint untuk mengecek data
@app.route('/data/<int:id>', methods=['GET'])
def check_data(id):
    # Cari data berdasarkan ID
    item = next((d for d in data if d['id'] == id), None)

    if item:
        # Jika data ditemukan
        return jsonify({
            "exists": True,
            "message": "Data found.",
            "data": item
        }), 200
    else:
        # Jika data tidak ditemukan
        return jsonify({
            "exists": False,
            "message": "Data not found."
        }), 404

# Jalankan server
if __name__ == '__main__':
    app.run(debug=True, port=3000)
