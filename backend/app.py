from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hellow_world():
	return "Hello world"

@app.route("/api/data")
def get_data():
	return jsonify({
		"message": "Flask data",
		"status": "success"
	})

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
